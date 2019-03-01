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
    errs = parser.getNumberOfSyntaxErrors()
    #print(parser.getNumberOfSyntaxErrors())
    #print(tree.toStringTree(recog=parser))
    result = open("result.txt", 'w')
    if errs != 0:
        result.write('Not accepted')
        print('Not accepted')
    else:
        result.write('Accepted')
        print('Accepted')
    result.close()

if __name__ == '__main__':
    main(sys.argv)
