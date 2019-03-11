#!/bin/bash

python3 -m venv antlr-env
source antlr-env/bin/activate
pip3 install antlr4-python3-runtime
cd antlr-env/lib/
cd ../../
eval 'wget https://www.antlr.org/download/antlr-4.7.2-complete.jar'

eval 'java -jar /antlr-env/bin/lib/antlr-4.7.2-complete.jar -Dlanguage=Python3 Tiny.g4'
./Scanner.py $1
