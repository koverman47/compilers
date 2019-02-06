#!/usr/bin/env python3

import sys
from antlr4 import *
from TinyLexer import TinyLexer
from TinyParser import TinyParser


def main(argv):
    input = FileStream(argv[1])
    lexer = TinyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TinyParser(stream)
    tree = parser.start()
    #printer = KeyPrinter()
    walker = ParseTreeWalker()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
