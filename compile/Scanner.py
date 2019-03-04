#!/usr/bin/env python3

from antlr4 import *
from Listener import Listener
from TinyLexer import TinyLexer
from TinyParser import TinyParser
import sys


def main(argv):
    inp = FileStream(argv[1])
    lexer = TinyLexer(inp)

    token_stream = CommonTokenStream(lexer)
    parser = TinyParser(token_stream)

    listener = Listener()

    tree = parser.program()
    walker = ParseTreeWalker().walk(listener, tree)
    print(listener.get_symbol_table())

if __name__ == '__main__':
    main(sys.argv)
