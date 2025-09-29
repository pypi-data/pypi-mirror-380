import argparse

from assistants import version
from assistants.config import environment


def get_args():
    parser = argparse.ArgumentParser(
        description=f"CLI for assistants-framework v{version.__VERSION__}",
        epilog=f"""
OPENAI_API_KEY environment variable {"must be set to use the OpenAI API (not set)" if not environment.OPENAI_API_KEY else "is set."}
{"ANTHROPIC_API_KEY environment variable must be set to use the Anthropic API (not set)" if environment.CODE_MODEL.startswith("claude-") and not environment.ANTHROPIC_API_KEY else "ANTHROPIC_API_KEY environment variable is set." if environment.ANTHROPIC_API_KEY and environment.CODE_MODEL.startswith("claude-") else ""}
""",
    )
    parser.add_argument(
        "prompt",
        nargs="*",
        help="positional arguments concatenate into a single prompt. E.g. `ai-cli "
        "Is this a single prompt\\?` (question mark escaped)\n"
        "...will be passed to the program as a single string (without the backslash). You "
        "can also use quotes to pass a single argument with spaces and special characters. "
        "See the -e and -f options for more advanced prompt options.",
    )
    parser.add_argument(
        "-e",
        "--editor",
        action="store_true",
        help="open the default editor to compose a prompt.",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="INPUT_FILE",
        type=str,
        help="read the initial prompt from a file (e.g., 'input.txt').",
    )
    parser.add_argument(
        "-t",
        "--continue-thread",
        action="store_true",
        help="continue previous thread.",
    )
    parser.add_argument(
        "-i",
        "--instructions",
        metavar="INSTRUCTIONS_FILE",
        type=str,
        help="read the initial instructions (system message) from a specified file; "
        "if this file is not provided, environment variable `ASSISTANT_INSTRUCTIONS` "
        "will be used (or a default of 'You are a helpful assistant').",
    )
    parser.add_argument(
        "-c",
        "--config-file",
        metavar="CONFIG_FILE",
        type=str,
        help="read config (instructions, model, thinking level, prompt etc.) from file. "
        "This is used to overwrite environment variables or command line arguments",
    )
    parser.add_argument(
        "-C",
        "--code",
        "--opus",
        action="store_true",
        help="use specialised reasoning/code model. WARNING: This model may be slower "
        "and more expensive to use (use the CODE_MODEL environment variable to change "
        "the model used. Defaults to 'o3-mini' with reasoning_effort set to 'high').",
    )
    parser.add_argument(
        "-m",
        "--model",
        metavar="MODEL",
        type=str,
        help="specify the model to use. Defaults to the environment variable DEFAULT_MODEL",
    )
    parser.add_argument(
        "-T",
        "--thinking",
        "--reasoning-effort",
        "--reasoning",
        nargs="?",
        const=1,
        default=0,
        type=int,
        help="whether to use thinking mode or not. In the case of OpenAI models this can "
        "be set to 2 for the highest level of thinking, 1 for medium, and so on. Defaults "
        "to 0, or 1 if passed without an argument.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version.__VERSION__}",
    )
    parser.add_argument("--debug", action="store_true", help="enable debug mode")
    args = parser.parse_args()
    return args
