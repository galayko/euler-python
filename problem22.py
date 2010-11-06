#!/usr/bin/env python
# Using names.txt, a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out
# the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938  53 = 49714.
# What is the total of all the name scores in the file?
import urllib2


def get_score(str):
    score = 0
    for i in range(len(str)):
        score += ord(str[i]) - ord('A') + 1
    return score

names_url = "http://projecteuler.net/project/names.txt"
stream = urllib2.urlopen(names_url)
str = stream.read()
stream.close()
names_list = str.split('","')
names_list[0] = names_list[0][1:]
names_list[-1] = names_list[-1][:-1]
names_list.sort()
scores_list = map(lambda x: get_score(x), names_list)
res = 0
for i in range(len(scores_list)):
    res += (i + 1) * scores_list[i]
print "RES=", res
