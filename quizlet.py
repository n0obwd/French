#!/usr/bin/env python

import random
from datetime import datetime


class quizObj(object):
    def __init__(self):
        self.filelen = 0
        self.topic_file = "topic.lib"
        self.topic_len = 42

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
        f = open(self.topic_file, "r")
        for line in f.readlines():
            if "\n" not in line:
                line = line + "\n"
            topic.append(line[:-1])
        f.close()
        for entry in topic:
            if searchWord in entry.lower():
                i = i + 1
                result.append(entry)
                print "%d. %s" % (i, entry)
        if i > 0:
            return result
        else:
            print ("No available topic. End now.")
            exit()

    def topic(self):
        i = 0
        topic = []
        searchWord = raw_input("Search for topic: ")
        if searchWord.lower() == "":
            print "List of topic: "
            print "=================="
            f = open(self.topic_file, "r")
            for line in f.readlines():
                i = i + 1
                if "\n" not in line:
                    line = line + "\n"
                print "%d. %s" % (i, line[:-1])
                topic.append(line[:-1])
            f.close()
            print "=================="
        else:
            topic = self.searchTopic(searchWord.lower())
        topicChoice = raw_input("Choose topic to practice: ")
        try:
            self.filename = "./lib/" + topic[int(topicChoice) - 1] + ".lib"
        except:
            print ("Incorrect input")
            exit()

    def randomize(self):
        f = open(self.filename, "r")
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
        for i in origin:
            f.write(i)
        f.close()

    def chooseWord(self, noOfWord):
        with open(self.filename) as f:
            for j, l in enumerate(f):
                pass
        f.close()
        self.filelen = int(j)
        f = open(self.filename, "r")
        raw = f.readlines()
        f.close()
        random.seed(datetime.now())
        collection = []
        for x in range(noOfWord):
            line = raw[random.randint(1, self.filelen) - 1]
            if line.endswith("\n"):
                line = line[:-1]
            rWord = {}
            rWord['fr'], rWord['def'] = line.split("--")
            collection.append(rWord)
        return collection


if __name__ == "__main__":
    quizObj = quizObj()
    topic = raw_input("Topic: ")
    print "Paste the content. Ctrl-Z to update"
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
