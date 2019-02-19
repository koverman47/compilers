#!/usr/bin/env python3

for i in range(1, 22):
    if i in [11, 13, 14]:
        continue
    f = open("test" + str(i) + ".out", 'r')
    for line in f:
        print(i, line)
    f.close()
