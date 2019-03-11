#!/bin/bash

eval 'wget https://www.antlr.org/download/antlr-4.7.2-complete.jar'
eval 'java -jar /usr/local/lib/antlr-4.7.2-complete.jar -Dlanguage=Python3 Tiny.g4'
./Scanner.py $1
