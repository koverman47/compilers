#!/bin/bash

python3 -m venv antlr-env
source antlr-env/bin/activate
pip3 install -qqq antlr4-python3-runtime
eval 'wget -q -nc https://www.antlr.org/download/antlr-4.7.2-complete.jar'

eval 'java -jar antlr-4.7.2-complete.jar -Dlanguage=Python3 Tiny.g4'
#eval 'java -jar /usr/local/lib/antlr-4.7.2-complete.jar -Dlanguage=Python3 Tiny.g4'
./Scanner.py $1
