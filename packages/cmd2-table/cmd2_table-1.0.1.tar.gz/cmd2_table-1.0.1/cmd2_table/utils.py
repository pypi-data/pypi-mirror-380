"""Shared utility functions."""

import collections
from enum import Enum

from cmd2_ansi import ansi

from . import constants


def _remove_overridden_styles(styles_to_parse: list[str]) -> list[str]:
    """Filter a style list down to only those which would still be in effect if all were processed in order.

    Utility function for align_text() / truncate_line().

    This is mainly used to reduce how many style strings are stored in memory when
    building large multiline strings with ANSI styles. We only need to carry over
    styles from previous lines that are still in effect.

    :param styles_to_parse: list of styles to evaluate.
    :return: list of styles that are still in effect.
    """

    class StyleState:
        """Keeps track of what text styles are enabled."""

        def __init__(self) -> None:
            # Contains styles still in effect, keyed by their index in styles_to_parse
            self.style_dict: dict[int, str] = {}

            # Indexes into style_dict
            self.reset_all: int | None = None
            self.fg: int | None = None
            self.bg: int | None = None
            self.intensity: int | None = None
            self.italic: int | None = None
            self.overline: int | None = None
            self.strikethrough: int | None = None
            self.underline: int | None = None

    # Read the previous styles in order and keep track of their states
    style_state = StyleState()

    for index, style in enumerate(styles_to_parse):
        # For styles types that we recognize, only keep their latest value from styles_to_parse.
        # All unrecognized style types will be retained and their order preserved.
        if style in (str(ansi.TextStyle.RESET_ALL), str(ansi.TextStyle.ALT_RESET_ALL)):
            style_state = StyleState()
            style_state.reset_all = index
        elif ansi.STD_FG_RE.match(style) or ansi.EIGHT_BIT_FG_RE.match(style) or ansi.RGB_FG_RE.match(style):
            if style_state.fg is not None:
                style_state.style_dict.pop(style_state.fg)
            style_state.fg = index
        elif ansi.STD_BG_RE.match(style) or ansi.EIGHT_BIT_BG_RE.match(style) or ansi.RGB_BG_RE.match(style):
            if style_state.bg is not None:
                style_state.style_dict.pop(style_state.bg)
            style_state.bg = index
        elif style in (
            str(ansi.TextStyle.INTENSITY_BOLD),
            str(ansi.TextStyle.INTENSITY_DIM),
            str(ansi.TextStyle.INTENSITY_NORMAL),
        ):
            if style_state.intensity is not None:
                style_state.style_dict.pop(style_state.intensity)
            style_state.intensity = index
        elif style in (str(ansi.TextStyle.ITALIC_ENABLE), str(ansi.TextStyle.ITALIC_DISABLE)):
            if style_state.italic is not None:
                style_state.style_dict.pop(style_state.italic)
            style_state.italic = index
        elif style in (str(ansi.TextStyle.OVERLINE_ENABLE), str(ansi.TextStyle.OVERLINE_DISABLE)):
            if style_state.overline is not None:
                style_state.style_dict.pop(style_state.overline)
            style_state.overline = index
        elif style in (str(ansi.TextStyle.STRIKETHROUGH_ENABLE), str(ansi.TextStyle.STRIKETHROUGH_DISABLE)):
            if style_state.strikethrough is not None:
                style_state.style_dict.pop(style_state.strikethrough)
            style_state.strikethrough = index
        elif style in (str(ansi.TextStyle.UNDERLINE_ENABLE), str(ansi.TextStyle.UNDERLINE_DISABLE)):
            if style_state.underline is not None:
                style_state.style_dict.pop(style_state.underline)
            style_state.underline = index

        # Store this style and its location in the dictionary
        style_state.style_dict[index] = style

    return list(style_state.style_dict.values())


class TextAlignment(Enum):
    """Horizontal text alignment."""

    LEFT = 1
    CENTER = 2
    RIGHT = 3


def align_text(
    text: str,
    alignment: TextAlignment,
    *,
    fill_char: str = ' ',
    width: int | None = None,
    tab_width: int = 4,
    truncate: bool = False,
) -> str:
    """Align text for display within a given width. Supports characters with display widths greater than 1.

    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    There are convenience wrappers around this function: align_left(), align_center(), and align_right()

    :param text: text to align (can contain multiple lines)
    :param alignment: how to align the text
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then each line will be shortened to fit within the display width. The truncated
                     portions are replaced by a '…' character. Defaults to False.
    :return: aligned text
    :raises TypeError: if fill_char is more than one character (not including ANSI style sequences)
    :raises ValueError: if text or fill_char contains an unprintable character
    :raises ValueError: if width is less than 1
    """
    import io
    import shutil

    if width is None:
        # Prior to Python 3.11 this can return 0, so use a fallback if needed.
        width = shutil.get_terminal_size().columns or constants.DEFAULT_TERMINAL_WIDTH

    if width < 1:
        raise ValueError("width must be at least 1")

    # Convert tabs to spaces
    text = text.replace('\t', ' ' * tab_width)
    fill_char = fill_char.replace('\t', ' ')

    # Save fill_char with no styles for use later
    stripped_fill_char = ansi.strip_style(fill_char)
    if len(stripped_fill_char) != 1:
        raise TypeError("Fill character must be exactly one character long")

    fill_char_width = ansi.style_aware_wcswidth(fill_char)
    if fill_char_width == -1:
        raise (ValueError("Fill character is an unprintable character"))

    # Isolate the style chars before and after the fill character. We will use them when building sequences of
    # fill characters. Instead of repeating the style characters for each fill character, we'll wrap each sequence.
    fill_char_style_begin, fill_char_style_end = fill_char.split(stripped_fill_char)

    lines = text.splitlines() if text else ['']

    text_buf = io.StringIO()

    # ANSI style sequences that may affect subsequent lines will be cancelled by the fill_char's style.
    # To avoid this, we save styles which are still in effect so we can restore them when beginning the next line.
    # This also allows lines to be used independently and still have their style. TableCreator does this.
    previous_styles: list[str] = []

    for index, line in enumerate(lines):
        if index > 0:
            text_buf.write('\n')

        if truncate:
            line = truncate_line(line, width)  # noqa: PLW2901

        line_width = ansi.style_aware_wcswidth(line)
        if line_width == -1:
            raise (ValueError("Text to align contains an unprintable character"))

        # Get list of styles in this line
        line_styles = list(get_styles_dict(line).values())

        # Calculate how wide each side of filling needs to be
        total_fill_width = 0 if line_width >= width else width - line_width
        # Even if the line needs no fill chars, there may be styles sequences to restore

        if alignment == TextAlignment.LEFT:
            left_fill_width = 0
            right_fill_width = total_fill_width
        elif alignment == TextAlignment.CENTER:
            left_fill_width = total_fill_width // 2
            right_fill_width = total_fill_width - left_fill_width
        else:
            left_fill_width = total_fill_width
            right_fill_width = 0

        # Determine how many fill characters are needed to cover the width
        left_fill = (left_fill_width // fill_char_width) * stripped_fill_char
        right_fill = (right_fill_width // fill_char_width) * stripped_fill_char

        # In cases where the fill character display width didn't divide evenly into
        # the gap being filled, pad the remainder with space.
        left_fill += ' ' * (left_fill_width - ansi.style_aware_wcswidth(left_fill))
        right_fill += ' ' * (right_fill_width - ansi.style_aware_wcswidth(right_fill))

        # Don't allow styles in fill characters and text to affect one another
        if fill_char_style_begin or fill_char_style_end or previous_styles or line_styles:
            if left_fill:
                left_fill = ansi.TextStyle.RESET_ALL + fill_char_style_begin + left_fill + fill_char_style_end
            left_fill += ansi.TextStyle.RESET_ALL

            if right_fill:
                right_fill = ansi.TextStyle.RESET_ALL + fill_char_style_begin + right_fill + fill_char_style_end
            right_fill += ansi.TextStyle.RESET_ALL

        # Write the line and restore styles from previous lines which are still in effect
        text_buf.write(left_fill + ''.join(previous_styles) + line + right_fill)

        # Update list of styles that are still in effect for the next line
        previous_styles.extend(line_styles)
        previous_styles = _remove_overridden_styles(previous_styles)

    return text_buf.getvalue()


def align_left(
    text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False
) -> str:
    """Left align text for display within a given width. Supports characters with display widths greater than 1.

    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to left align (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: left-aligned text
    :raises TypeError: if fill_char is more than one character (not including ANSI style sequences)
    :raises ValueError: if text or fill_char contains an unprintable character
    :raises ValueError: if width is less than 1
    """
    return align_text(text, TextAlignment.LEFT, fill_char=fill_char, width=width, tab_width=tab_width, truncate=truncate)


def align_center(
    text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False
) -> str:
    """Center text for display within a given width. Supports characters with display widths greater than 1.

    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to center (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: centered text
    :raises TypeError: if fill_char is more than one character (not including ANSI style sequences)
    :raises ValueError: if text or fill_char contains an unprintable character
    :raises ValueError: if width is less than 1
    """
    return align_text(text, TextAlignment.CENTER, fill_char=fill_char, width=width, tab_width=tab_width, truncate=truncate)


def align_right(
    text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False
) -> str:
    """Right align text for display within a given width. Supports characters with display widths greater than 1.

    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to right align (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: right-aligned text
    :raises TypeError: if fill_char is more than one character (not including ANSI style sequences)
    :raises ValueError: if text or fill_char contains an unprintable character
    :raises ValueError: if width is less than 1
    """
    return align_text(text, TextAlignment.RIGHT, fill_char=fill_char, width=width, tab_width=tab_width, truncate=truncate)


def truncate_line(line: str, max_width: int, *, tab_width: int = 4) -> str:
    """Truncate a single line to fit within a given display width.

    Any portion of the string that is truncated is replaced by a '…' character. Supports characters with display widths greater
    than 1. ANSI style sequences do not count toward the display width.

    If there are ANSI style sequences in the string after where truncation occurs, this function will append them
    to the returned string.

    This is done to prevent issues caused in cases like: truncate_line(Fg.BLUE + hello + Fg.RESET, 3)
    In this case, "hello" would be truncated before Fg.RESET resets the color from blue. Appending the remaining style
    sequences makes sure the style is in the same state had the entire string been printed. align_text() relies on this
    behavior when preserving style over multiple lines.

    :param line: text to truncate
    :param max_width: the maximum display width the resulting string is allowed to have
    :param tab_width: any tabs in the text will be replaced with this many spaces
    :return: line that has a display width less than or equal to width
    :raises ValueError: if text contains an unprintable character like a newline
    :raises ValueError: if max_width is less than 1
    """
    import io

    # Handle tabs
    line = line.replace('\t', ' ' * tab_width)

    if ansi.style_aware_wcswidth(line) == -1:
        raise (ValueError("text contains an unprintable character"))

    if max_width < 1:
        raise ValueError("max_width must be at least 1")

    if ansi.style_aware_wcswidth(line) <= max_width:
        return line

    # Find all style sequences in the line
    styles_dict = get_styles_dict(line)

    # Add characters one by one and preserve all style sequences
    done = False
    index = 0
    total_width = 0
    truncated_buf = io.StringIO()

    while not done:
        # Check if a style sequence is at this index. These don't count toward display width.
        if index in styles_dict:
            truncated_buf.write(styles_dict[index])
            style_len = len(styles_dict[index])
            styles_dict.pop(index)
            index += style_len
            continue

        char = line[index]
        char_width = ansi.style_aware_wcswidth(char)

        # This char will make the text too wide, add the ellipsis instead
        if char_width + total_width >= max_width:
            char = constants.HORIZONTAL_ELLIPSIS
            char_width = ansi.style_aware_wcswidth(char)
            done = True

        total_width += char_width
        truncated_buf.write(char)
        index += 1

    # Filter out overridden styles from the remaining ones
    remaining_styles = _remove_overridden_styles(list(styles_dict.values()))

    # Append the remaining styles to the truncated text
    truncated_buf.write(''.join(remaining_styles))

    return truncated_buf.getvalue()


def get_styles_dict(text: str) -> dict[int, str]:
    """Return an OrderedDict containing all ANSI style sequences found in a string.

    The structure of the dictionary is:
        key: index where sequences begins
        value: ANSI style sequence found at index in text

    Keys are in ascending order

    :param text: text to search for style sequences
    """
    start = 0
    styles = collections.OrderedDict()

    while True:
        match = ansi.ANSI_STYLE_RE.search(text, start)
        if match is None:
            break
        styles[match.start()] = match.group()
        start += len(match.group())

    return styles
