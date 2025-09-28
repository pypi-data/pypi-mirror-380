#!/usr/bin/env python3

"""
Executes the server with all arguments.

If extending, consider calling the cli module directly
instead. This module will execute with all arguments
passed without restriction.
"""

if __name__ == "__main__":
    from . import cli

    cli.main()


__all__ = tuple()
