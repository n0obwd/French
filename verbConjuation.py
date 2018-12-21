#!/usr/bin/env python
# -*- coding: utf- -*-

from verb import *


class vConj(object):
    def __init__(self):
        self.verb = ""
        self.db = []
        self.dbbase = []
        self.getDB()
        self.ipart = ""

    # get list of base verb database and classify database
    def getDB(self):
        fn = open("verb.lib", "r")
        fn.readline()
        for line in fn.readlines():
            line = list(ast.literal_eval(line))
            self.db.append(line)
        fn.close()
        for verb in self.db:
            self.dbbase.append(verb[0])
            if verb[0] == "aller":
                verb.append(3)
                continue
            if verb[0][-2:] == "er":
                verb.append(1)
                continue
            if verb[0] == "finir" or verb[0] == "agir" or verb[0] == "reagir" or verb[0] == "haïr" or verb[0] == "obéir":
                verb.append(2)
            else:
                verb.append(3)

    def predict(self, verb):
        i = 0
        bestIdentical = 0
        listIndentical = []
        if verb in self.dbbase:
            listIndentical.append(verb)
        else:
            for word in self.dbbase:
                identical = 0
                i = 1
                while i < len(word):
                    if verb[::-1].startswith(word[::-1][:i]):
                        identical += 1
                    i = i + 1
                percentage = float(identical) / len(word) * 100
                if percentage > bestIdentical:
                    bestIdentical = percentage
                    listIndentical = []
                    listIndentical.append(word)
                    self.ipart = verb[-identical:]
                else:
                    if percentage == bestIdentical:
                        listIndentical.append(word)
        return listIndentical

    def conjugation(self, verb, tense):
        listIndentical = self.predict(verb)
        verbObject = verbObj()
        conjList = []
        if len(listIndentical) == 1:
            baseConj = verbObject.conjugation(listIndentical[0], tense)
            for i in range(0, 7):
                conjList.append(baseConj[i].replace(listIndentical[0].replace(
                    self.ipart, ""), verb.replace(self.ipart, ""), 1))
        else:
            print listIndentical
        return conjList


if __name__ == "__main__":
    vConj = vConj()
    verb = raw_input("Verb: ")
    tense = int(raw_input("Tense: "))
    for i in vConj.conjugation(verb, tense):
        print i
