#!/usr/bin/env python
# A Pythagorean triplet is a set of three natural numbers, a  < b  < c,
# for which, a^(2) + b^(2) = c^(2)
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# There exists exactly one Pythagorean triplet for which a+b+c = 1000.
# Find the product abc.

def isPythagorean(a, b, c):
    if (a**2+b**2)==c**2: return True
    return False

def getPythagoreanTripletProduct(ressum):
    for a in range(1, ressum+1):
        for b in range(a+1, ressum-a+1):
            c = ressum - a - b
            if isPythagorean(a, b, c):
                if (a+b+c)==ressum:
                    return a*b*c
    return -1

print getPythagoreanTripletProduct(1000)
