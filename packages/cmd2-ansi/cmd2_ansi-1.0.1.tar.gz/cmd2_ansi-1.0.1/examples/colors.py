#!/usr/bin/env python
"""A sample application for cmd2-ansi demonstrating colorized output."""

from cmd2_ansi import (
    Bg,
    Fg,
    ansi,
)

if __name__ == '__main__':
    print(ansi.style("This is a test", fg=Fg.BLUE, bold=True))
    print(ansi.style("of the emergency broadcast system", bg=Bg.RED))
