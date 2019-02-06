#!/usr/bin/env python3

import sys
from antlr4 import *
from TinyLexer import TinyLexer
from TinyParser import TinyParser


def main(argv):
    inp = FileStream(argv[1])
    lexer = TinyLexer(inp)
    #stream = CommonTokenStream(lexer)
    #parser = TinyParser(stream)
    #tree = parser.start()
    #printer = KeyPrinter()
    #walker = ParseTreeWalker()
    #print(tree.toStringTree(recog=parser))
    tokens = lexer.getAllTokens()
    for token in tokens:
        #print(token.type, token.text)
        print(token)

if __name__ == '__main__':
    main(sys.argv)
