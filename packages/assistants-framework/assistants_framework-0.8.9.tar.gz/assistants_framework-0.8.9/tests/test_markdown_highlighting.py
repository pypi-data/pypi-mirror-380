from pygments import highlight
from pygments.lexers import TextLexer
try:
    from pygments.lexers.markup import MarkdownLexer
except ImportError:
    from pygments.lexers.markup_lexer import MarkdownLexer
from pygments.formatters import TerminalFormatter
try:
    from pygments.formatters import TerminalTrueColorFormatter
except ImportError:
    TerminalTrueColorFormatter = None

def print_highlighted(text, lexer, formatter):
    print(f"\n--- {formatter.__class__.__name__} ({getattr(formatter, 'style', None)}) ---")
    print(highlight(text, lexer, formatter))

def main():
    md = """# Heading 1\n\nSome **bold** text, some *italic* text, and some `inline code`.\n\n```python\ndef foo():\n    return 'bar'\n```\n\nNormal text again."""
    print("Original Markdown:\n", md)
    print_highlighted(md, MarkdownLexer(), TerminalFormatter())
    print_highlighted(md, MarkdownLexer(), TerminalFormatter(style="monokai"))
    if TerminalTrueColorFormatter:
        print_highlighted(md, MarkdownLexer(), TerminalTrueColorFormatter(style="monokai"))

if __name__ == "__main__":
    main()

