#!/usr/bin/env python3

from antlr4 import *
from TinyLexer import TinyLexer
from TinyParser import TinyParser
import sys


def main(argv):
    inp = FileStream(argv[1])
    lexer = TinyLexer(inp)

    token_stream = CommonTokenStream(lexer)
    parser = TinyParser(token_stream)
    tree = parser.program()

    print(parser.getNumberOfSyntaxErrors())


if __name__ == '__main__':
    main(sys.argv)
