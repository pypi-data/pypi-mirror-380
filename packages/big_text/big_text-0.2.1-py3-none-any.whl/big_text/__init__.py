# SPDX-FileCopyrightText: 2025 Geoffrey Lentner
# SPDX-License-Identifier: MIT

"""Convert text to ASCII art."""


# Type annotations
from __future__ import annotations
from typing import Final, List, Optional

# Standard libs
import sys
from importlib.metadata import version as get_version
from functools import partial
from platform import python_implementation, python_version

# External libs
from cmdkit.cli import Interface
from cmdkit.app import Application, exit_status
from cmdkit.logging import Logger, level_by_name, logging_styles

# Internal libs
from big_text.data import Font, font_map

# Public interface
__all__ = [
    '__version__',
    'BigText', 'main',
    'ascii_art', 'Font', 'font_map',
]

# Metadata
__version__ = get_version('big-text')


log = Logger.default(name=__name__, level=level_by_name['INFO'], **logging_styles['default'])


def print_exception(exc: Exception, status: int) -> int:
    """Log `exc` and return `status`."""
    log.critical(str(exc))
    return status


def ascii_art(text: str, font: Font = font_map['big']) -> str:
    """Convert text to ASCII art."""
    letters = [font.data[letter] for letter in text.upper().strip()]
    return '\n'.join([
        ' '.join([letter[i] for letter in letters])
        for i in range(font.rows)
    ])


PROGRAM: Final[str] = 'big-text'
VERSION: Final[str] = f'{PROGRAM} v{__version__} ({python_implementation()} {python_version()})'
USAGE: Final[str] = f"""\
Usage:
  {PROGRAM} [-vh] TEXT [--big | --mini]
  {__doc__}\
"""
HELP: Final[str] = f"""\
{USAGE}

Options:
      --big                Use big style font (default).
      --mini               Use mini style font.
  -v, --version            Show version info and exit.
  -h, --help               Show this message and exit.\
"""


class BigText(Application):
    """Application interface."""

    interface = Interface(PROGRAM, USAGE, HELP)
    interface.add_argument('-v', '--version', action='version', version=VERSION)

    text: str
    interface.add_argument('text')

    font: str = 'big'
    interface.add_argument('--big', action='store_const', const='big', dest='font', default='big')
    interface.add_argument('--mini', action='store_const', const='mini', dest='font')

    include_padding: bool = False
    interface.add_argument('-p', '--padding', action='store_true', dest='include_padding')

    log_critical = log.critical
    log_exception = log.exception
    exceptions = {
        RuntimeError: partial(print_exception, status=exit_status.runtime_error),
        Exception: partial(print_exception, status=exit_status.uncaught_exception),
    }

    def run(self: BigText) -> None:
        """Run program."""
        print(ascii_art(self.text, font=font_map[self.font]))


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry-point for the program."""
    return BigText.main(argv or sys.argv[1:])
