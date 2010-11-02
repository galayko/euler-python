#!/usr/bin/env python
# n! means n  (n  1)  ...  3  2  1
# Find the sum of the digits in the number 100!

n = 100
n = reduce(lambda x, y: x*y, range(1,n+1))
summ =  reduce(lambda x, y: int(x)+int(y), list(str(n)))
print "Res=", summ
