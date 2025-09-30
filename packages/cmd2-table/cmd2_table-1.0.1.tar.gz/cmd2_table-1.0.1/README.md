<h1 align="center">cmd2-table : Backport of cmd2.table_creator module from cmd2 2.7.0 to ease migration to cmd2 3.x</h1>

[![Latest Version](https://img.shields.io/pypi/v/cmd2-table.svg?style=flat-square&label=latest%20stable%20version)](https://pypi.python.org/pypi/cmd2-table/)
[![GitHub Actions](https://github.com/python-cmd2/cmd2-table/workflows/Tests/badge.svg)](https://github.com/python-cmd2/cmd2-table/actions?query=workflow%3ATests)

cmd2-table is a backport of the cmd2.table_creator module from cmd2 2.7.0. It exists to ease the
migration from cmd2 2.x to cmd2 3.x. In cmd2 3.x, there is no built-in table creation functionality
since cmd2 now has a dependency on [rich](https://github.com/Textualize/rich) which has great
support for creating tables.
