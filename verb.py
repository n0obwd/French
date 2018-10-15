#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
import argparse
import sys
import ast
import random
import re
from datetime import datetime


class verbObj(object):
    def __init__(self):
        self.tense = ["present", "passe-compose", "imparfait",
                      "plus-que-parfait", "futur-simple", "futur-anterieur"]
        self.person = ["1", "2", "3", "4", "5", "6", "7"]
        self.file = "verb.lib"
        self.vowel = ["a", "o", "e", "i", "u"]
        self.person = ["je", "tu", "il", "nous", "vous", "ils"]
        self.add = [" me ", " te ", " se ", " nous ", " vous ", " se "]
        self.addVowel = [" m'", " t'", " s'", " nous ", " vous ", " s'"]

    def filelen(self, filename):
        with open(filename) as f:
            for i, l in enumerate(f):
                pass
        return str(i)

    def update_line(self, filename, number):
        wording = "@number:" + number + "\n"
        for line in fileinput.input(filename, inplace=1):
            if "@number" in line:
                line = wording
            sys.stdout.write(line)

    def add_word(self, filename):
        line = ""
        new = raw_input("infinitif: ")
        opt1 = " " + new + "\""
        opt2 = "\"" + new + "\""
        f = open(filename, "r")
        isExist = 0
        for x in f.readlines():
            if opt1 in x:
                isExist = 1
            if opt2 in x:
                isExist = 1
        f.close()
        if isExist == 0:
            line = line + "\"" + new + "\",\""
            for ctr2 in range(0, len(self.person)):
                wording = self.tense[0] + self.person[ctr2] + ": "
                line = line + raw_input(wording) + "\",\""
            line = line[:-2]
            print line
            f = open(filename, "a")
            f.write("\n")
            f.write(line)
            f.close()
        else:
            print "%s is already in the list" % new

    def update_word(self, filename, word):
        user_input = int(raw_input("What person to update [1-7]: "))
        new = raw_input("Update: ")
        f = open(filename, "r")
        raw = []
        i = f.readline()
        raw.append(i[:-1])
        for i in f.readlines():
            i = list(ast.literal_eval(i))
            if i[0] == word:
                i[user_input] = new
            i = "\n\"" + '\",\"'.join(i)
            i = i + "\""
            raw.append(i)
        f.close()
        f = open(filename, "w")
        for i in raw:
            line = ''.join(i)
            f.write(line)

    def show_word(self, filename, word):
        f = open(filename, "r")
        f.readline()
        isExist = 0
        for i in f.readlines():
            i = list(ast.literal_eval(i))
            if i[0] == word:
                isExist = 1
                print "infinitif: " + i[0]
                for j in range(1, 7):
                    print "present" + str(j) + ": " + i[j]
                print "participe passe: " + i[7]
        if isExist == 0:
            print "It's not in the list yet"

    def randomize(self, filename):
        f = open(filename, "r")
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
        f = open(filename, "w")
        f.write(first_line)
        for i in origin:
            f.write(i)
        f.close()

    def find_word(self, word):
        aux = []
        f = open(self.file, "r")
        f.readline()
        for i in f.readlines():
            i = list(ast.literal_eval(i))
            if i[0] == word:
                for j in range(0, 8):
                    aux.append(i[j])
                break
        f.close()
        return aux

    def chooseAux(self, word):
        house = {"naître", "devenir", "mourir", "descendre", "rester", "monter", "tomber", "venir",
                 "arriver", "entre", "aller", "sortir", "partir", "revenir", "rentre", "retourner", "passer"}
        if word in house or word[0:3] == "se " or word[0:2] == "s'":
            aux_choice = "être"
        else:
            aux_choice = "avoir"
        return aux_choice

    def conjugation(self, word, tenseNo):
        conj = []
        conj.append(word)
        wordPre = self.find_word(word)
        pp = wordPre[7]
        # present
        if tenseNo == 0:
            for i in range(1, 7):
                conj.append(self.find_word(word)[i])
        # passé composé
        if tenseNo == 1:
            aux = self.find_word(self.chooseAux(word))
            for i in range(1, 7):
                conj.append(aux[i] + " " + pp)
            if aux[0] == "être":
                for i in range(1, 7):
                    if word[0:3] == "se " or word[0:2] == "s'":
                        added = [" me ", " t'", " s'",
                                 " nous ", " vous ", " se "]
                        conj[i] = conj[i].replace(" ", added[i - 1], 1)
                    if i > 3:
                        conj[i] = conj[i] + "s"
        # imparfait
        if tenseNo == 2:
            suffix = ["ais", "ais", "ait", "ions", "iez", "aient"]
            added = ["m'", "t'", "s'", "", "", "s'"]
            if word == "pleuvoir" or word == "falloir":
                prefix = word[:-3]
            else:
                prefix = wordPre[4].rsplit(" ", 1)[1][:-3]
            if word == "être":
                prefix = "ét"
            prefixExemp = prefix
            if prefix[-2:] == "ge":
                prefixExemp = prefix[:-1]
            if prefix[-2:] == "ç":
                prefixExemp = prefix.replace("ç", "c")
            for i in range(1, 7):
                prefixAdd = prefix
                prefixExempAdd = prefixExemp
                if word[0:2] == "s'":
                    prefixAdd = added[i - 1] + prefix
                    prefixExempAdd = added[i - 1] + prefixExemp
                if i == 4 or i == 5:
                    conj.append(wordPre[i].rsplit(" ", 1)[
                        0] + " " + prefixExempAdd + suffix[i - 1])
                else:
                    conj.append(wordPre[i].rsplit(" ", 1)[
                                0] + " " + prefixAdd + suffix[i - 1])
            if word[0:1] in self.vowel or (word[0:2] == "ha" and word[0:4] != "haï") or prefix[0:2] == "é":
                conj[1] = "j'" + conj[1].split(" ", 1)[1]

        # plus-que-parfait
        if tenseNo == 3:
            aux = self.find_word(self.chooseAux(word))
            aux = self.conjugation(aux[0], 2)
            for i in range(1, 7):
                conj.append(aux[i] + " " + pp)
            if aux[0] == "être":
                for i in range(1, 7):
                    if word[0:3] == "se " or word[0:2] == "s'":
                        if i == 1:
                            conj[i] = conj[i].replace("'", "e ", 1)
                        conj[i] = conj[i].replace(" ", self.addVowel[i - 1], 1)
                    if i > 3:
                        conj[i] = conj[i] + "s"
        # futur-simple
        if tenseNo == 4:
            original = word
            suffix = ["ai", "as", "a", "ons", "ez", "ont"]
            wordEx = ["être", "avoir", "recevoir", "voir", "pourvoir", "savoir", "devoir", "pouvoir", "pleuvoir", "falloir", "valoir",
                      "vouloir", "s'asseoir", "s'asseoir(2)", "aller", "envoyer", "venir", "acquérir", "cueillir", "courir", "mourir", "souvenir"]
            prefixEx = ["sere", "aure", "recevre", "verre", "pourvoire", "saure", "devre", "pourre", "pleuvre", "faudre", "vaudre",
                        "voudre", "s'assiére", "s'assoire", "ire", "enverre", "viendre", "acquerre", "cueillere", "courre", "mourre", "souviendre"]
            filler = [" ", " ", " ", " ", " ", " "]
            if word in wordEx:
                word = prefixEx[wordEx.index(word)]
            if word[0:3] == "se ":
                word = word[3:]
                filler = self.add
            if word[0:2] == "s'":
                word = word[2:]
                filler = self.addVowel


            if word[-2:] == "re":
                for i in range(1, 7):
                    conj.append(
                        self.person[i - 1] + filler[i - 1] + word[:-1] + suffix[i - 1])

            if word[-2:] == "er":
                if re.search("e[a-z]er", word) or word[-3:] == "yer":
                    word = self.find_word(word)[3].split(" ", 1)[1] + "r"
                for i in range(1, 7):
                    conj.append(self.person[i - 1] +
                                filler[i - 1] + word + suffix[i - 1])

            if word[-2:] == "ir" or word[-3:] == "ïr":
                for i in range(1, 7):
                    conj.append(self.person[i - 1] +
                                filler[i - 1] + word + suffix[i - 1])

            if original[0:1] in self.vowel or (original[0:2] == "ha" and original[0:4] != "haï") or word[0:2] == "é":
                conj[1] = "j'" + conj[1].split(" ", 1)[1]

        # futur-antérieur
        if tenseNo == 5:
            aux = self.find_word(self.chooseAux(word))
            aux = self.conjugation(aux[0], 4)
            for i in range(1, 7):
                conj.append(aux[i] + " " + pp)
            if aux[0] == "être":
                for i in range(1, 7):
                    if word[0:3] == "se " or word[0:2] == "s'":
                        added = [" me ", " te ", " se ",
                                 " nous ", " vous ", " se "]
                        conj[i] = conj[i].replace(" ", added[i - 1], 1)
                    if i > 3:
                        conj[i] = conj[i] + "s"

        if word == "pleuvoir" or word == "falloir" or word == "pleuvre" or word == "faudre":
            for i in range(1, 7):
                if i != 3:
                    conj[i] = ""
        return conj


if __name__ == "__main__":
    f = "verb.lib"
    verb = verbObj()
    parser = argparse.ArgumentParser(description='Word list task')
    parser.add_argument('-a', '--add', dest='task', action='store_const',
                        const='new_word', help='New word')
    parser.add_argument('-u', '--update', dest='task', action='store_const',
                        const='update_word', help="Upate word")
    parser.add_argument('-s', '--show', dest='task', action='store_const',
                        const='show_word', help="Show word")
    parser.add_argument('-w', dest='word', help="Word")
    parser.add_argument('-r', '--random', dest='task', action='store_const',
                        const='randomize', help="Randomize all words")
    parser.add_argument('-c', '--conjugation', dest='task',
                        action='store_const', const='conjugation', help='Verb conjugation')
    parser.add_argument('-v', dest="word", help="verb")
    parser.add_argument('-t', dest="tense", help="tense")
    args = vars(parser.parse_args())
    if args['task'] == 'show_word':
        verb.show_word(f, args['word'])
    if args['task'] == 'update_word':
        verb.update_word(f, args['word'])
    if args['task'] == 'new_word':
        verb.add_word(f)
        verb.update_line(f, verb.filelen(f))
    if args['task'] == 'randomize':
        verb.randomize(f)
    if args['task'] == 'conjugation':
        for i in verb.conjugation(args["word"], int(args["tense"])):
            print i
