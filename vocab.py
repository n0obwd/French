#!/usr/bin/env python
# -*- coding: utf- -*-

import random
import ast
import argparse
from datetime import datetime
from time import sleep
from multiprocessing.pool import ThreadPool
import sys

from verb import *
from numero import *
from nationalite import *
from quizlet import *


def verbConj1(noOfWord, collection):
    vTense = ["present", "passé composé", "imparfait",
              "plus-que-parfait", "futur simple", "futur antérieur"]
    random.seed(datetime.now())
    score = 0
    verb = verbObj()
    for i in range(noOfWord):
        wrong = []
        print "=================="
        word = collection[i - 1][0]
        qTense = random.randint(0, 5)
        qList = verb.conjugation(word, qTense)
        print "Infinitif: %s" % word
        print "Tense: %s" % vTense[qTense]
        right = 1
        for j in range(1, 7):
            question = "%d: " % j
            answer = raw_input(question)
            if answer == qList[j]:
                right = right * 1
            else:
                right = right * 0
                wrong.append(j)
        score = score + right
        if len(wrong) == 0:
            print "All's good"
        else:
            for x in wrong:
                print "Wrong %d: %s" % (x, qList[x])

    return score


def verbConj2(noOfWord, collection):
    score = 0
    vTense = ["present", "passé composé", "imparfait",
              "plus-que-parfait", "futur simple", "futur antérieur"]
    # ------------------------------------ #
    random.seed(datetime.now())
    verb = verbObj()
    try:
        for i in range(noOfWord):
            print "=================="
            word = collection[i - 1][0]
            flag = ""
            if "(2)" in word:
                flag = "*"
            qTense = random.randint(0, 5)
            qPerson = random.randint(1, 6)
            qConj = verb.conjugation(word, qTense)[qPerson]
            if qConj == "":
                qConj = verb.conjugation(word, qTense)[3] + "*"
            print "%d. %s %d: %s%s" % (i + 1, vTense[qTense], qPerson, qConj, flag)
            answer = raw_input("Infinitif: ")
            if answer == word:
                random.seed(datetime.now())
                aTense = random.randint(0, 5)
                aPerson = random.randint(1, 6)
                aConj = verb.conjugation(word, aTense)[aPerson]
                if aConj == "":
                    aPerson = 3
                    aConj = verb.conjugation(word, aTense)[aPerson]
                display = "%s %d: " % (vTense[aTense], aPerson)
                answer = raw_input(display)
                if answer == aConj:
                    score = score + 1
                    print "Correct"
                else:
                    print "Wrong. %s %d: %s" % (vTense[aTense], aPerson, aConj)
            else:
                print "Wrong. Infinitif: %s" % word
    except:
        print word
        print qTense
        print qPerson
    return score


def timer():
    for i in range(10):
        print i
        sleep(1)
    sys.exit()


def chooseWord(filename, noOfWord):
    verb = verbObj()
    collection = []
    verb.randomize(filename)
    f = open(filename, 'r')
    raw = f.readlines()
    f.close()
    random.seed(datetime.now())
    for x in range(noOfWord):
        line = raw[random.randint(1, int(verb.filelen(filename)))]
        rWord = ast.literal_eval(line)
        collection.append(rWord)
    return collection


def random_games(tense, noOfWord, collection):
    random.seed(datetime.now())
    score = 0
    for i in range(noOfWord):
        print "=================="
        ranTense = random.randint(1, 7)
        print "Infinitif: %s" % collection[i - 1][0]
        answer = raw_input(tense[ranTense - 1] + " is: ")
        correct = collection[i - 1][ranTense]
        if correct == "":
            correct = collection[i - 1][3]
        if answer == correct:
            score = score + 1
            print "Correct"
        else:
            print "Not correct: \n" + correct
    return score


def reverse(tense, noOfWord, collection):
    random.seed(datetime.now())
    score = 0
    for i in range(noOfWord):
        print "=================="
        qTense = random.randint(1, 7)
        if collection[i - 1][1] == "":
            qTense = 3
        print "%s: %s" % (tense[qTense - 1], collection[i - 1][qTense])
        answer_inf = raw_input("Infinitif: ")
        if answer_inf == collection[i - 1][0]:
            aTense = random.randint(1, 7)
            while aTense == qTense:
                aTense = random.randint(1, 7)
            answer_prTense = raw_input(tense[aTense - 1] + " is: ")
            correct_prTense = collection[i - 1][aTense]
            if correct_prTense == 0:
                correct_prTense = collection[i - 1][3]
            if answer_prTense == correct_prTense:
                score = score + 1
                print "Correct"
            else:
                print "Not correct"
                print "Correct %s is: %s" % (tense[aTense - 1], correct_prTense)
        else:
            print "Not correct: %s" % collection[i - 1][0]
    return score


def instant(tense, noOfWord, collection):
    random.seed(datetime.now())
    score = 0
    for i in range(noOfWord):
        print "=================="
        qTense = random.randint(1, 7)
        if collection[i - 1][1] == "":
            qTense = 3
        print "%s: %s" % (tense[qTense - 1], collection[i - 1][qTense])
        aTense = random.randint(1, 7)
        while aTense == qTense:
            aTense = random.randint(1, 7)
        answer_prTense = raw_input(tense[aTense - 1] + " is: ")
        correct_prTense = collection[i - 1][aTense]
        if correct_prTense == 0:
            correct_prTense = collection[i - 1][3]
        if answer_prTense == correct_prTense:
            score = score + 1
            print "Correct"
        else:
            print "Not correct"
            print "Correct %s is: %s" % (tense[aTense - 1], correct_prTense)
    return score


def numero(noOfWord):
    number = numeroObj()
    number.randomize()
    score = 0
    collection = number.chooseWord(noOfWord)
    for i in range(noOfWord):
        print "=================="
        answer = raw_input("%s: " % collection[i]["number"])
        correct_ans = collection[i]["word"]
        if answer == correct_ans:
            score = score + 1
            print "Correct"
        else:
            print "Not correct"
            print "%s: %s" % (collection[i]["number"], correct_ans)
    return score


def nation(noOfWord):
    natObj = nationaliteObj()
    natObj.randomize()
    score = 0
    collection = natObj.chooseWord(noOfWord)
    for i in range(noOfWord):
        print "=================="
        answer1 = raw_input("%s (mas): " % collection[i]["pays"])
        answer2 = raw_input("%s (fem): " % collection[i]["pays"])
        correct_ans1 = collection[i]["masNat"]
        correct_ans2 = collection[i]["femNat"]
        if answer1 != correct_ans1:
            print "Not correct:"
            print "%s (mas) %s" % (collection[i]["pays"], correct_ans1)
            right1 = 0
        else:
            right1 = 1
        if answer2 != correct_ans2:
            print "Not correct:"
            print "%s (fem) %s" % (collection[i]["pays"], correct_ans2)
            right2 = 0
        else:
            right2 = 1
        score = score + right1 * right2
    return score


def numero_10(noOfWord):
    number = numeroObj()
    random.seed(datetime.now())
    score = 0
    for i in range(noOfWord):
        print "=================="
        question = random.randint(0, 1000**4)
        answer = raw_input("{:,}".format(question) + ": ")
        number.iniOrigin(question)
        correct_ans = number.formNumber(question)
        if answer == correct_ans:
            score = score + 1
            print "Correct"
        else:
            print "Not correct"
            print "%s: %s" % ("{:,}".format(question), correct_ans)
    return score


def quizlet(noOfWord):
    score = 0
    quiz = quizObj()
    quiz.topic()
    quiz.randomize()
    collection = quiz.chooseWord(noOfWord)
    for i in range(noOfWord):
        print "=================="
        question = collection[i]['def']
        answer = raw_input(question + ": ")
        correct_ans = collection[i]['fr']
        if answer == correct_ans:
            score = score + 1
            print "Correct"
        else:
            print "Not correct"
            print "%s: %s" % (correct_ans, question)
    return score


def learn(tense, noOfWord, collection):
    for i in range(noOfWord):
        answer = []
        wrong = []
        print "=================="
        print "%d.Infinitif: %s" % (i + 1, collection[i - 1][0])
        answer.append(collection[i - 1][0])
        for j in range(1, 8):
            answer.append(raw_input(tense[j - 1] + " is: "))
            if answer[j] != collection[i - 1][j]:
                wrong.append(j)
        if len(wrong) == 0:
            print "All's good"
        else:
            for x in wrong:
                print "Wrong %s: %s" % (tense[x - 1], collection[i - 1][x])


if __name__ == "__main__":
    print "Time for some French"
    pTense = ["present1", "present2", "present3",
              "present4", "present5", "present6", "participe passe"]
    filename = "verb.lib"

    parser = argparse.ArgumentParser(description='Word list task')
    parser.add_argument('-v', '--verb', dest='task', action='store_const',
                        const='verb', help='Learn new word')
    parser.add_argument('--thuy1', dest='task', action='store_const',
                        const='conjugation1', help='Conjugation all tenses')
    parser.add_argument('--thuy2', dest='task', action='store_const',
                        const='conjugation2', help='Conjugation all tenses - Reflex')
    parser.add_argument('-a', '--game1', dest='task', action='store_const',
                        const='a', help="Game1: Infinitif -> Random tense")
    parser.add_argument('-b', '--game2', dest='task', action='store_const',
                        const='b', help="Random tense -> Infinitif -> Random tense")
    parser.add_argument('-c', '--game3', dest='task', action='store_const',
                        const='c', help="Random tense -> Random tense")
    parser.add_argument('-d', '--game4', dest='task', action='store_const',
                        const='d', help="Number 0-100")
    parser.add_argument('-e', '--game5', dest='task',
                        action='store_const', const='e', help='Number 0-1000000')
    parser.add_argument('-f', '--game6', dest='task', action='store_const',
                        const='f', help="Nationalite")
    parser.add_argument('-q', '--quiz', dest='task', action='store_const',
                        const='q', help="Learn vocabulary from Quizlet")
    parser.add_argument('-w', '--word', dest='word', help="Number of words")
    args = vars(parser.parse_args())

    if args['task'] == "verb":
        learn(pTense, int(args['word']), chooseWord(
            filename, int(args['word'])))
        print "*********************"
    else:
        if args['task'] == "a":
            finalScore = random_games(pTense, int(
                args['word']), chooseWord(filename, int(args['word'])))
        if args['task'] == "b":
            finalScore = reverse(pTense, int(
                args['word']), chooseWord(filename, int(args['word'])))
        if args['task'] == "c":
            finalScore = instant(pTense, int(
                args['word']), chooseWord(filename, int(args['word'])))
        if args['task'] == "d":
            filename = "numero.lib"
            finalScore = numero(int(args['word']))
        if args['task'] == "e":
            finalScore = numero_10(int(args['word']))
        if args['task'] == "f":
            finalScore = nation(int(args['word']))
        if args['task'] == "conjugation1":
            finalScore = verbConj1(
                int(args['word']), chooseWord(filename, int(args['word'])))
        if args['task'] == "conjugation2":
            finalScore = verbConj2(
                int(args['word']), chooseWord(filename, int(args['word'])))
        if args['task'] == "q":
            finalScore = quizlet(int(args['word']))
        print "*********************"
        print "Final score: %d/%d" % (finalScore, int(args['word']))
        if finalScore < int(args['word']):
            print "You suck"
        else:
            print "Good job. No treat though. Goodluck next time"
