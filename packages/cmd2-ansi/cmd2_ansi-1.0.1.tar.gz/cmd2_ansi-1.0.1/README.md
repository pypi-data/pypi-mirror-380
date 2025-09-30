<h1 align="center">cmd2-ansi : Backport of cmd2.ansi module from cmd2 2.7.0 to ease migration to cmd2 3.x</h1>

[![Latest Version](https://img.shields.io/pypi/v/cmd2-ansi.svg?style=flat-square&label=latest%20stable%20version)](https://pypi.python.org/pypi/cmd2-ansi/)
[![GitHub Actions](https://github.com/python-cmd2/cmd2-ansi/workflows/Tests/badge.svg)](https://github.com/python-cmd2/cmd2-ansi/actions?query=workflow%3ATests)

cmd2-ansi is a backport of the cmd2.ansi module from cmd2 2.7.0. It exists to ease the migration
from cmd2 2.x to cmd2 3.x. In cmd2 3.x, there is a dependency on
[rich](https://github.com/Textualize/rich) which has great support for creating pretty ansi
formatting.
