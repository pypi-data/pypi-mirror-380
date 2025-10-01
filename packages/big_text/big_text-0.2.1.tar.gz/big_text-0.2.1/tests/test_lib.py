# SPDX-FileCopyrightText: 2025 Geoffrey Lentner
# SPDX-License-Identifier: MIT

"""Test ascii_art functionality."""


# Type annotations
from __future__ import annotations
from typing import Final, List

# External libs
from pytest import mark

# Internal libs
from big_text import ascii_art, font_map


HELLO_BIG: Final[str] = """\
██╗  ██╗ ███████╗ ██╗      ██╗       ██████╗ 
██║  ██║ ██╔════╝ ██║      ██║      ██╔═══██╗
███████║ ███████╗ ██║      ██║      ██║   ██║
██╔══██║ ██╔════╝ ██║      ██║      ██║   ██║
██║  ██║ ███████╗ ███████╗ ███████╗ ╚██████╔╝
╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚══════╝  ╚═════╝ \
"""

HELLO_MINI: Final[str] = """\
╓ ╓ ╔══ ╓   ╓   ╭═╮
╠═╣ ╠══ ║   ║   ║ ║
╜ ╜ ╚══ ╚══ ╚══ ╰═╯\
"""


@mark.unit
def test_hello_big() -> None:
    """Test text conversion to ASCII art."""
    assert HELLO_BIG == ascii_art('hello')
    assert HELLO_BIG == ascii_art('Hello')
    assert HELLO_BIG == ascii_art('HELLO')
    assert HELLO_BIG == ascii_art(' HELLO  ')
    assert HELLO_BIG == ascii_art('hello', font=font_map['big'])
    assert HELLO_BIG == ascii_art('Hello', font=font_map['big'])
    assert HELLO_BIG == ascii_art('HELLO', font=font_map['big'])
    assert HELLO_BIG == ascii_art(' HELLO  ', font=font_map['big'])


@mark.unit
def test_hello_mini() -> None:
    """Test text conversion to ASCII art."""
    assert HELLO_MINI == ascii_art('hello', font=font_map['mini'])
    assert HELLO_MINI == ascii_art('Hello', font=font_map['mini'])
    assert HELLO_MINI == ascii_art('HELLO', font=font_map['mini'])
    assert HELLO_MINI == ascii_art(' HELLO  ', font=font_map['mini'])


ANSWER_BIG: Final[str] = """\
 █████╗  ███╗  ██╗  ██████╗ ██╗     ██╗ ███████╗ ██████╗             ██╗  ██╗ ██████╗ 
██╔══██╗ ████╗ ██║ ██╔════╝ ██║     ██║ ██╔════╝ ██╔══██╗  ██╗       ██║  ██║ ╚════██╗
██║  ██║ ██╔██╗██║ ╚█████╗  ██║  █  ██║ ███████╗ ██████╔╝  ╚═╝       ███████║  █████╔╝
███████║ ██║╚████║  ╚═══██╗ ██║ ███ ██║ ██╔════╝ ██╔══██╗            ╚════██║ ██╔═══╝ 
██╔══██║ ██║ ╚███║ ██████╔╝  ███╔═╗██║  ███████╗ ██║  ██║  ██╗            ██║ ███████╗
╚═╝  ╚═╝ ╚═╝  ╚══╝ ╚═════╝   ╚══╝ ╚══╝  ╚══════╝ ╚═╝  ╚═╝  ╚═╝            ╚═╝ ╚══════╝\
"""


ANSWER_MINI: Final[str] = """\
╔═╗ ╔╮ ╖ ╭═╮ ╖  ╓ ╔══ ╔═╮ •     ╔ ╗ ╒═╮
╠═╣ ║╚╗║ ╰═╮ ║╔╗║ ╠══ ║╦╯       ╚═╣ ╭═╝
╜ ╜ ╜ ╰╝ ╰═╯ ╚╝╚╝ ╚══ ╝╚═ •       ╜ ╚══\
"""


@mark.unit
def test_answer_big() -> None:
    """Test text conversion to ASCII art."""
    assert ANSWER_BIG == ascii_art('answer: 42')
    assert ANSWER_BIG == ascii_art('Answer: 42')
    assert ANSWER_BIG == ascii_art('ANSWER: 42')
    assert ANSWER_BIG == ascii_art('ANSWER: 42  ')
    assert ANSWER_BIG == ascii_art('answer: 42', font=font_map['big'])
    assert ANSWER_BIG == ascii_art('Answer: 42', font=font_map['big'])
    assert ANSWER_BIG == ascii_art('ANSWER: 42', font=font_map['big'])
    assert ANSWER_BIG == ascii_art('ANSWER: 42  ', font=font_map['big'])


@mark.unit
def test_answer_mini() -> None:
    """Test text conversion to ASCII art."""
    assert ANSWER_MINI == ascii_art('answer: 42', font=font_map['mini'])
    assert ANSWER_MINI == ascii_art('Answer: 42', font=font_map['mini'])
    assert ANSWER_MINI == ascii_art('ANSWER: 42', font=font_map['mini'])
    assert ANSWER_MINI == ascii_art('ANSWER: 42  ', font=font_map['mini'])
