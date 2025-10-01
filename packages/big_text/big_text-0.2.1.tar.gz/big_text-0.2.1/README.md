```
██████╗  ██╗  ██████╗          ████████╗ ███████╗ ██╗  ██╗ ████████╗
██╔══██╗ ██║ ██╔════╝          ╚══██╔══╝ ██╔════╝ ╚██╗██╔╝ ╚══██╔══╝
██████╔╝ ██║ ██║  ███╗  █████╗    ██║    ███████╗  ╚███╔╝     ██║   
██╔══██╗ ██║ ██║   ██║  ╚════╝    ██║    ██╔════╝  ██╔██║     ██║   
██████╔╝ ██║ ╚██████╔╝            ██║    ███████╗ ██╔╝╚██╗    ██║   
╚═════╝  ╚═╝  ╚═════╝             ╚═╝    ╚══════╝ ╚═╝  ╚═╝    ╚═╝   
```


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
&nbsp;
[![Version](https://img.shields.io/github/v/release/glentner/big-text?sort=semver)](https://github.com/glentner/big-text)
&nbsp;
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads)


A Python library and command-line tool for converting text into ASCII art.


Install
-------

The well-known [uv](https://docs.astral.sh/uv/) utility is the best way to install this program.

```sh
uv tool install big-text
```


Usage
-----

Use `big-text --help` to get usage and help on options.

```sh
big-text 'Welcome!'
```

To use within another Python project, `uv add big-text`:

```python
from big_text import ascii_art

text = ascii_art('Welcome!')
print(text)
```


Note
----

Ported from original MATLAB code:
> Eli Farber (2025). makeBanner - Big ASCII Style Comment Generator.
> MATLAB Central File Exchange. Retrieved September 22, 2025.
> URL: https://www.mathworks.com/matlabcentral/fileexchange/181715-makebanner-big-ascii-style-comment-generator)