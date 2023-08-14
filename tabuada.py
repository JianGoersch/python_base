#!/usr/bin/env python3

__version__="0.1.0"
__author__="Jian Goersch"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

base = list(range(1,11))

#iterable (percorriveis)

for n in base:
    print("Tabuada do: ", n)
    for multiplicando in base:
        print(multiplicando * n)
    print("---------------")    