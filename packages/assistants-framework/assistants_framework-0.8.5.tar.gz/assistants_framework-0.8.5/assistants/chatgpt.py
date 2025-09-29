import asyncio
import os
import sys

from assistants.cli import run_cli
from assistants.config import environment
from assistants.user_data.sqlite_backend import init_db

CHATGPT_MODEL = os.getenv("DEFAULT_CHATGPT_MODEL", "gpt-5-mini")
CHATGPT_REASONING_MODEL = os.getenv("DEFAULT_GPT_REASONING_MODEL", "o4-mini")


def main():
    if not environment.OPENAI_API_KEY:
        print("OPENAI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)
    environment.DEFAULT_MODEL = CHATGPT_MODEL
    environment.CODE_MODEL = CHATGPT_REASONING_MODEL
    asyncio.run(init_db())
    run_cli()


if __name__ == "__main__":
    main()
