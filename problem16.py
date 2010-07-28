#!/usr/bin/env python
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

n = 2**1000
s = "%s" % n
summ = 0
for char in s: summ+=int(char)
print "Res=", summ
