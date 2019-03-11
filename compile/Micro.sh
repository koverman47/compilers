#!/bin/bash

python3 -m venv antlr-env
source antlr-env/bin/activate
pip3 install antlr4-python3-runtime
cd antlr-env/bin/
curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
cd ../../

eval 'java -jar /antlr-env/bin/antlr-4.7.2-complete.jar -Dlanguage=Python3 Tiny.g4'
./Scanner.py $1
