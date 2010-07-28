#!/usr/bin/env python
# n! means n  (n  1)  ...  3  2  1
# Find the sum of the digits in the number 100!

n = 1
for i in range(1,101): n*=i
s = "%s" % n
summ = 0
for char in s: summ+=int(char)
print "Res=", summ
