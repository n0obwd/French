#!/usr/bin/env python

import random
from datetime import datetime


class nationaliteObj(object):
    def __init__(self):
        self.filename = "nationalite.lib"

    def randomize(self):
        f = open(self.filename, "r")
        first_line = f.readline()
        origin = []
        for i in f.readlines():
            if "\n" in i:
                origin.append(i)
            else:
                j = i + "\n"
                origin.append(j)
        f.close()
        random.seed(datetime.now())
        random.shuffle(origin)
        origin[-1] = origin[-1][:-1]
        f = open(self.filename, "w")
        f.write(first_line)
        for i in origin:
            f.write(i)
        f.close()

    def chooseWord(self, noOfWord):
        f = open(self.filename, "r")
        raw = f.readlines()
        f.close()
        random.seed(datetime.now())
        collection = []
        for x in range(noOfWord):
            line = raw[random.randint(1, 63) - 1]
            if line.endswith("\n"):
                line = line[:-1]
            rWord = {}
            rWord['pays'], rWord['masNat'], rWord['femNat'] = line.split(":")
            collection.append(rWord)
        return collection


if __name__ == "__main__":
    natObjt = nationaliteObj()
    pass
