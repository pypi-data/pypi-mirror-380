from typing import Optional
from openai import OpenAI
from .config import get_api_key
import os

SYSTEM_MSG = (
    "You are an expert code translator across programming frameworks."
    "Given source code, emit ONLY the target framework code that is behaviorally equivalent."
    "Do not include explanations, comments, or markdown—output code only."
)

def client(api_key: Optional[str] = None) -> None:
    key = api_key or get_api_key()
    if not key:
        raise RuntimeError("OpenAI API key not configured. Run `ft init` first.")
    os.environ["OPENAI_API_KEY"] = key

def translate_code(
    framework_code: str,
    target_framework: str,
    language: str,
    framework_group: str,
    source_framework: Optional[str] = None,
) -> str:
    client()
    src_fw = source_framework or None
    prompt = (
        f"Language: {language}\n"
        f"Framework group: {framework_group}\n"
        f"Task: Translate the following {language} code from {src_fw} to {target_framework}.\n"
        "Requirements:\n"
        "- Preserve behavior and public API surface when reasonable.\n"
        "- Do NOT include explanations, comments, or markdown—return ONLY the translated code.\n"
        "- If certain APIs do not exist in the target, provide the closest idiomatic equivalent.\n"
        "Source code is delimited by +++\n"
        f"+++{framework_code}+++"
    )
    openai_client = OpenAI()
    response = openai_client.responses.create(
        model="gpt-5",
        reasoning={"effort": "medium"},
        input=prompt,
        instructions=SYSTEM_MSG,
    )
    return response.output_text
