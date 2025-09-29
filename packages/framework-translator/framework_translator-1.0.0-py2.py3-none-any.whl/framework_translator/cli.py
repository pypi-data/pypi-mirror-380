import argparse
import sys
from getpass import getpass
from typing import Optional
from .config import (
    load_config,
    set_api_key,
    check_first_run,  # added
)
from .model import translate_code
from termcolor import colored

# Supported language/group/framework mappings
SUPPORTED_LANGUAGES = ["python"]
LANGUAGE_GROUPS = {
    "python": ["ml"],
}
GROUP_FRAMEWORKS = {
    "ml": ["jax", "tensorflow", "pytorch", "scikit-learn"],
}

def get_supported_languages() -> list[str]:
    return SUPPORTED_LANGUAGES

def get_supported_groups(language: str) -> list[str]:
    return LANGUAGE_GROUPS.get(language.lower(), [])

def get_supported_frameworks(group: str) -> list[str]:
    return GROUP_FRAMEWORKS.get(group.lower(), [])

def _read_code_from_stdin() -> str:
    print(colored("Paste source code. Finish with Ctrl-D (Linux/macOS) or Ctrl-Z+Enter (Windows).", "cyan"))
    return sys.stdin.read()

def _read_code_from_prompt() -> str:
    print(colored("Enter source code (end with a single line containing only 'END'):", "cyan"))
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def cmd_init(args: argparse.Namespace) -> int:
    print(colored("Setup: Framework Translator", "green"))
    key = getpass(colored("OpenAI API key: ", "cyan"))
    if not key:
        print(colored("No API key provided.", "red"), file=sys.stderr)
        return 1

    set_api_key(key)
    _ = load_config() 
    print(colored("API key saved locally (encrypted and secured).", "green"))
    print(colored("You are all set! You can now use the `ft translate` command to translate code across frameworks.", "green"))
    return 0

def cmd_translate(args: argparse.Namespace) -> int:
    print(colored("Translate: Framework Translator", "green"))
    print(colored("Ensure you have run `ft init` to configure your OpenAI API key.", "yellow"))
    print(colored("WARNING: This operation may incur costs on your OpenAI account based on usage.", "red"))
    language = input(colored(f"Choose a language -> Languages supported [{', '.join(get_supported_languages())}]: ", "cyan")).strip().lower()
    if not language:
        language = "python"

    source_framework = input(colored("Give us your framework: (Enter to let the model infer): ", "cyan")).strip()
    source_framework = source_framework or None
    
    group = input(colored(f"Choose a framework group -> Framework groups supported for language {language} [{', '.join(get_supported_groups(language))}]: ", "cyan")).strip().lower()
    if not group:
        group = "ml"

    target_framework = input(colored(f"Choose a target framework -> Target frameworks supported for group {group} [{', '.join(get_supported_frameworks(group))}]: ", "cyan")).strip()
    if not target_framework:
        print(colored("Target framework is required.", "red"), file=sys.stderr)
        return 1


    code: str
    print(colored("Provide source code via one of the options:", "yellow"))
    print(colored("1) Paste (end with 'END' on its own line)", "cyan"))
    print(colored("2) File path", "cyan"))
    choice = input(colored("Select [1/2]: ", "yellow")).strip()
    if choice == "2":
        path = input(colored("Enter file path: ", "cyan")).strip()
        try:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception as e:
            print(colored(f"Failed to read file: {e}", "red"), file=sys.stderr)
            return 1
    else:
        code = _read_code_from_prompt()

    print(colored(f"Translating code to {target_framework}...", "yellow"))

    try:
        output = translate_code(
            framework_code=code,
            target_framework=target_framework,
            language=language,
            framework_group=group,
            source_framework=source_framework,
        )
        print(colored("--------------------------------------", "green"))
        print(colored("----------Translation Result----------", "green"))
        print(colored("--------------------------------------", "green"))
        print(output)
        print(colored("--------------------------------------", "green"))
        print(colored("Translation completed successfully.", "green"))
        return 0
    except Exception as e:
        print(colored(f"Translation failed: {e}", "red"), file=sys.stderr)
        return 2

def main(argv: Optional[list[str]] = None) -> int:
    check_first_run()  # print welcome only on first run
    parser = argparse.ArgumentParser(prog="ft", description="Translate code across frameworks using an OpenAI fine-tuned model.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Store your OpenAI API key locally (encrypted).")
    p_init.set_defaults(func=cmd_init)

    p_tx = sub.add_parser("translate", help="Translate source code to a target framework.")
    p_tx.set_defaults(func=cmd_translate)

    def _cmd_help(args: argparse.Namespace) -> int:
        if getattr(args, "topic", None) == "translate":
            p_tx.print_help()
        else:
            parser.print_help()
        return 0

    p_help = sub.add_parser("help", help="Show general help or help for a specific subcommand.")
    p_help.add_argument("topic", nargs="?", choices=["translate"], help="Subcommand to show help for (e.g., 'translate').")
    p_help.set_defaults(func=_cmd_help)

    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())