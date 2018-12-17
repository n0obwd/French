#!/usr/bin/env python

import random
from datetime import datetime


class quizObj(object):
    def __init__(self):
        self.filelen = 0
        self.topic_file = "topic.lib"
        self.topic_len = 42
        self.choosenTopic = []

    def filehandling(self, topic, content):
        content = content.replace("\n", " ; ")
        content = content.replace("::", "\n")
        content = content[:-1]
        exist = 0
        f = open(self.topic_file, "r")
        for line in f.readlines():
            if "\n" in line:
                line = line[:-1]
            if line == topic:
                exist = 1
        f.close()
        if exist == 0:
            f = open(self.topic_file, "a")
            f.write("\n" + topic)
            f.close()
        name = "./lib/" + topic + ".lib"
        f = open(name, "w+")
        f.write(content)
        f.close()

    def searchTopic(self, searchWord):
        topic = []
        result = []
        i = 0
        j = 0
        f = open(self.topic_file, "r")
        for line in f.readlines():
            if "\n" not in line:
                line = line + "\n"
            topic.append(line[:-1])
        f.close()
        for entry in topic:
            j = j + 1
            if searchWord.isdigit():
                if int(searchWord) == j:
                    result.append(entry)
                    return result
            if searchWord in entry.lower():
                i = i + 1
                result.append(entry)
        if i > 0:
            return result
        else:
            print ("No available topic. End now.")
            exit()

    def topic(self):
        i = 0
        topic = []
        fullTopic = []
        self.choosenTopic = []
        skipChoose = 1
        searchWord = raw_input("Search for topic: ")
        # Get full list of all topic
        f = open(self.topic_file, "r")
        for line in f.readlines():
            if "\n" not in line:
                line = line + "\n"
            fullTopic.append(line[:-1])
        f.close()

        if searchWord.lower() == "":
            # If no search word, meaning display the full list
            topic = fullTopic
            skipChoose = 0
        else:
            # strip all ", " to filer the input
            sWordList = [x.strip() for x in searchWord.split(',')]
            for entry in sWordList:
                # If entry is number, save the topic with
                # same order in full list to choosenTopic list
                if entry.isdigit():
                    self.choosenTopic.append(
                        "./lib/" + fullTopic[int(entry) - 1] + ".lib")
                    skipChoose = skipChoose * 1
                    continue
                # To handle range input using "-"
                if "-" in entry:
                    s, r = entry.split("-")
                    try:
                        for j in range(int(s), int(r) + 1):
                            fn = "./lib/" + fullTopic[j - 1] + ".lib"
                            self.choosenTopic.append(fn)
                        skipChoose = skipChoose * 1
                        continue
                    except Exception as e:
                        print ("Incorrect input")
                        exit()
                # If search input is not number, search the word.
                if entry.isalpha():
                    topic = topic + self.searchTopic(entry)
                    skipChoose = skipChoose * 0

        # display topics for user to choose
        if skipChoose == 0:
            # remove duplicated topics
            for x in self.choosenTopic:
                x = x[6:][:-4]
                if x not in topic:
                    topic.append(x)
            self.choosenTopic = []
            i = 0
            for e in topic:
                i = i + 1
                print "%d. %s" % (i, e)
            userChoice = raw_input("Choose your topic: ")
            choiceList = [y.strip() for y in userChoice.split(',')]
            for item in choiceList:
                try:
                    if "-" in item:
                        s, r = item.split("-")
                        for j in range(int(s), int(r) + 1):
                            fn = "./lib/" + topic[j - 1] + ".lib"
                            self.choosenTopic.append(fn)
                    else:
                        self.choosenTopic.append(
                            "./lib/" + topic[int(item) - 1] + ".lib")
                except Exception as e:
                    print ("Incorrect input")
                    exit()

    def randomize(self):
        for fn in self.choosenTopic:
            f = open(fn, "r")
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
            f = open(fn, "w")
            for i in origin:
                f.write(i)
            f.close()

    def chooseWord(self, noOfWord):
        raw = []
        for fn in self.choosenTopic:
            with open(fn) as f:
                for j, l in enumerate(f):
                    pass
            f.close()
            self.filelen = self.filelen + int(j)
            f = open(fn, "r")
            raw = raw + f.readlines()
            f.close()
        random.seed(datetime.now())
        collection = []
        for x in range(noOfWord):
            line = raw[random.randint(1, self.filelen) - 1]
            if line.endswith("\n"):
                line = line[:-1]
            rWord = {}
            rWord['fr'], rWord['def'] = line.split("--")
            if rWord in collection:
                line = raw[random.randint(1, self.filelen) - 1]
                if line.endswith("\n"):
                    line = line[:-1]
                rWord['fr'], rWord['def'] = line.split("--")
            collection.append(rWord)
        return collection


if __name__ == "__main__":
    quizObj = quizObj()
    topic = raw_input("Topic: ")
    print "Paste the content. Ctrl-C to update"
    contents = []
    while True:
        try:
            line = raw_input("")
            contents.append(line)
        except KeyboardInterrupt:
            content = "\n".join(contents)
            quizObj.filehandling(topic, content)
            break

    pass
