#!/usr/bin/env python
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two
# 3-digit numbers.
x = 111
y = 111
prod = i*j
while x<1000:
    y = 111
    while y<1000:
        tmp = x*y
        stmp = str(tmp)
        if stmp == stmp[::-1]:
            if tmp>prod:
                prod = tmp
        y+=1
    x+=1
print 'Result=',prod
