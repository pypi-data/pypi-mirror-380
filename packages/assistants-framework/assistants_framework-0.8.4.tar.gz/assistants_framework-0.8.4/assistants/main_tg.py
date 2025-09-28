import asyncio
import os
import sys

from assistants.config import environment
from assistants.log import logger
from assistants.user_data.sqlite_backend import init_db

try:
    from assistants.telegram_ui.tg_bot import setup_and_run
except ImportError:
    logger.error(
        "Could not import required modules. Install with `pip install assistants[telegram]`"
    )
    sys.exit(1)


def main():
    if environment.TELEGRAM_BOT_TOKEN is None:
        print("Please set the TG_BOT_TOKEN environment variable.")
        return

    os.environ.setdefault("TELEGRAM_DATA", "1")
    asyncio.run(init_db())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    environment.ASSISTANT_INSTRUCTIONS = f"""\
Users interact with you through Telegram. Their messages will be prefixed with their name; 
however, you should not prefix your responses with your own name in the same way.
{environment.ASSISTANT_INSTRUCTIONS}
"""
    setup_and_run(environment.TELEGRAM_BOT_TOKEN)


if __name__ == "__main__":
    main()
