#!/usr/bin/env python

import random
import math
from datetime import datetime


class numeroObj(object):
    def __init__(self):
        self.filename = "numero.lib"
        self.fixWord = ["", "mille", "million",
                        "milliard", "billion", "billiard"]
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
        if numb > 0:
            self.logarithm = int(math.floor(math.log(self.origin, 1000)))
        else:
            self.logarithm = 0
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

    def find_number(self, numb, iszero):
        if numb == 0 and iszero == 0:
            return ""
        numb = str(numb)
        with open(self.filename, "r") as ins:
            for line in ins:
                if numb in line:
                    new_str = line.replace(numb, " ")
                    if new_str[:2] == " :":
                        if new_str.endswith("\n"):
                            return new_str[2:][:-1]
                        else:
                            return new_str[2:]

    def numtoword(self, number):
        if number <= 100:
            return self.find_number(number, 0)
        else:
            if number < 200:
                result = "cent " + self.find_number(number % 100, 0)
            else:
                if number % 100 == 0:
                    result = self.find_number(number // 100, 0) + " cents"
                else:
                    result = self.find_number(
                        number // 100, 0) + " cent " + self.find_number(number % 100, 0)
            return result

    def formNumber(self, number):
        if number == 0:
            return self.find_number(0, 1)
        word = ""
        numList = []
        wordList = []
        for exp in range(1, self.logarithm + 1):
            target = number
            while target >= 1000**exp:
                target = target % (1000**exp)
                if exp > 1:
                    target = target // (1000**(exp - 1))
                numList.append(target)
                wordList.append(self.numtoword(target))
        numList.append(number // 1000**self.logarithm)
        wordList.append(self.numtoword(number // 1000**self.logarithm))
        numList.reverse()
        wordList.reverse()
        for i in range(0, len(numList)):
            if numList[i] == 0:
                continue
            connector = self.fixWord[len(numList) - i - 1]
            if numList[i] > 1 and connector != "mille" and connector != "":
                connector = connector + "s"
            word = word + wordList[i] + " " + connector + " "
        return word[:-2]


if __name__ == "__main__":
    numObj = numeroObj()
    no = int(raw_input("Number: "))
    numObj.iniOrigin(no)
    print numObj.formNumber(no)
