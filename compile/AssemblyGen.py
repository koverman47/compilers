#!/usr/bin/env python3

from antlr4 import *
from Listener import Listener
from TinyLexer import TinyLexer
from TinyParser import TinyParser
from Three2Two import convert

import sys


def main(argv):
    inp = FileStream(argv[1])
    lexer = TinyLexer(inp)

    token_stream = CommonTokenStream(lexer)
    parser = TinyParser(token_stream)

    listener = Listener()

    tree = parser.program()
    walker = ParseTreeWalker().walk(listener, tree)

    lines = []
    assembly_code = listener.assembly_code
    for i in range(len(assembly_code)):
        while assembly_code[i]:
            line = assembly_code[i].pop()
            print(line)
            lines.append(line)
    #convert(lines)


if __name__ == '__main__':
    main(sys.argv)
