import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from platformdirs import user_config_dir
from cryptography.fernet import Fernet
import stat

APP_NAME = "framework_translator"
APP_AUTHOR = "strasta"

def _config_path() -> Path:
    cfg_dir = Path(user_config_dir(APP_NAME, APP_AUTHOR))
    cfg_dir.mkdir(parents=True, exist_ok=True)
    return cfg_dir / "config.json"

def load_config() -> Dict[str, Any]:
    path = _config_path()
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}

def save_config(cfg: Dict[str, Any]) -> None:
    path = _config_path()
    path.write_text(json.dumps(cfg, indent=2))
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)  # 0o600
    except Exception:
        pass

def get_encryption_key() -> bytes:
    cfg = load_config()
    if "encryption_key" not in cfg:
        key = Fernet.generate_key()
        cfg["encryption_key"] = key.decode()
        save_config(cfg)
    return cfg["encryption_key"].encode()

def encrypt(data: str) -> str:
    return Fernet(get_encryption_key()).encrypt(data.encode()).decode()

def decrypt(token: str) -> str:
    return Fernet(get_encryption_key()).decrypt(token.encode()).decode()

def get_api_key(cfg: Optional[Dict[str, Any]] = None) -> Optional[str]:
    env_key = os.environ.get("OPENAI_API_KEY")
    if env_key:
        return env_key
    cfg = cfg or load_config()
    enc = cfg.get("enc_openai_api_key")
    if enc:
        try:
            return decrypt(enc)
        except Exception:
            return None
    return cfg.get("openai_api_key")

def set_api_key(key: str) -> None:
    cfg = load_config()
    cfg["enc_openai_api_key"] = encrypt(key.strip())
    cfg.pop("openai_api_key", None) 
    save_config(cfg)
    cfg = load_config()
    save_config(cfg)

def check_first_run() -> None:
    cfg = load_config()
    if cfg.get("first_run", True):
        print("Welcome to the Framework Translator CLI!")
        print("Use `ft help` to see available commands.")
        cfg["first_run"] = False
        save_config(cfg)