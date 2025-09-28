import sys
from dataclasses import dataclass
from enum import Enum
import re

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import StyleAndTextTuples
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.document import Document

from assistants.cli.fs import FilesystemService
from assistants.config.file_management import CONFIG_DIR


class PromptStyle(Enum):
    USER_INPUT = "ansigreen"
    PROMPT_SYMBOL = "ansibrightgreen"


INPUT_CLASSNAME = "input"


class AtPathLexer(Lexer):
    """Lexer to highlight filesystem paths starting with '@'."""

    def lex_document(self, document: Document):
        """Highlight @-paths in the document."""
        path_pattern = FilesystemService.FILE_TAG_REGEX

        def get_line(lineno):
            line = document.lines[lineno]
            tokens = []
            last = 0
            for m in re.finditer(path_pattern, line):
                if m.start() > last:
                    tokens.append(("class:text", line[last : m.start()]))
                tokens.append(("class:atpath", line[m.start() : m.end()]))
                last = m.end()
            if last < len(line):
                tokens.append(("class:text", line[last:]))
            return tokens

        return get_line


@dataclass
class PromptConfig:
    """Configuration for the interactive prompt."""

    style: Style = Style.from_dict(
        {
            "": PromptStyle.USER_INPUT.value,
            INPUT_CLASSNAME: PromptStyle.PROMPT_SYMBOL.value,
            "atpath": "ansiblue bold",
            "text": PromptStyle.USER_INPUT.value,
        }
    )
    prompt_symbol: str = ">>>"
    history_file: str = f"{CONFIG_DIR}/history"


bindings = KeyBindings()
config = PromptConfig()
history = FileHistory(config.history_file)
PROMPT: StyleAndTextTuples = [(f"class:{INPUT_CLASSNAME}", f"{config.prompt_symbol} ")]


@bindings.add("tab")
def cmpl(event: KeyPressEvent):
    """Auto-complete filesystem paths starting with '@'."""
    full_text = event.current_buffer.text
    cursor_position = event.current_buffer.cursor_position
    words = full_text[:cursor_position].split()
    current_word = words[-1] if words else ""
    if current_word and FilesystemService.is_fs_ref(current_word):
        path = current_word[1:]  # Remove the '@' prefix
        completed_path = FilesystemService.auto_complete_path(path)
        event.app.current_buffer.delete_before_cursor(len(current_word))
        event.app.current_buffer.insert_text(f"@{completed_path}")


def get_user_input() -> str:
    """Get user input from interactive/styled prompt (prompt_toolkit)."""
    if not sys.stdin.isatty():
        sys.stdin = open("/dev/tty")
    return prompt(
        PROMPT,
        style=config.style,
        history=history,
        key_bindings=bindings,
        lexer=AtPathLexer(),
        in_thread=True,
    )
