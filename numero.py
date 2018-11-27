#!/usr/bin/env python

import random
import math
from datetime import datetime


class numeroObj(object):
    def __init__(self):
        self.filename = "numero.lib"
        self.fixWord = ["mille", "million", "milliard"]
        self.logarithm = 0
        self.origin = 0

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

    def iniOrigin(self, numb):
        self.origin = int(numb)
        self.logarithm = int(math.floor(math.log(self.origin, 1000)))
        return 1

    def chooseWord(self, noOfWord):
        f = open(self.filename, "r")
        raw = f.readlines()
        f.close()
        random.seed(datetime.now())
        collection = []
        for x in range(noOfWord):
            line = raw[random.randint(1, 104) - 1]
            if "\n" in line:
            	line = line[:-1]
            rWord = {}
            rWord['number'], rWord['word'] = line.split(":")
            collection.append(rWord)
        return collection

    def find_number(self, numb):
        with open(self.filename, "r") as ins:
            for line in ins:
                if numb in line:
                    new_str = line.replace(numb, " ")
                    if new_str[:2] == " :":
                        if new_str.endswith("\n"):
                            return new_str[2:][:-1]
                        else:
                            return new_str[2:]

    def formNumber(self, number):
        word = ""
        if number == 0 and self.origin > 0:
            return word
        if number > 1000 and number != 1000000 and number != 1000000000:
            if self.logarithm == 1:
                if number >= 2000:
                    word = self.formNumber(
                        number // 1000) + " " + self.fixWord[self.logarithm - 1] + " " + word + self.formNumber(number % 1000)
                else:
                    word = word + \
                        self.fixWord[self.logarithm] + " " + \
                        self.formNumber(number % 1000)
            else:
                self.logarithm = self.logarithm - 1
                prefix = self.formNumber(number // 1000)
                if prefix.endswith("un") and not prefix.endswith("et un") and not prefix.endswith("et un "):
                    word = prefix + " " + \
                        self.fixWord[self.logarithm] + \
                        " " + word + self.formNumber(number % 1000)
                else:
                    word = prefix + " " + \
                        self.fixWord[self.logarithm] + \
                        "s " + word + self.formNumber(number % 1000)

        else:
            if number <= 100 or number == 1000 or number == 1000000 or number == 1000000000:
                return self.find_number(str(number))
            if number < 200:
                word = "cent " + self.formNumber(number % 100)
                return word
            else:
                if number % 100 == 0:
                    word = self.formNumber(number // 100) + " cents"
                else:
                    word = self.formNumber(number // 100) + \
                        " cent " + self.formNumber(number % 100)
                return word
        return word


if __name__ == "__main__":
    numObj = numeroObj()
    no = int(raw_input("Number: "))
    numObj.iniOrigin(no)
    print numObj.formNumber(no)
