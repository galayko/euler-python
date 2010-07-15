#!/usr/bin/env python
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
def isprime(num):
    tmp = 2
    while tmp<num:
        if num%tmp==0:
            return False
        tmp+=1
    return True


m = 600851475143
n = 3
while m/n>1:
    if n%3==0 or n%5==0 or n%7==0 or n%11==0 or n%13==0 or n%17==0 or n%19==0 or n%23==0:
        n+=2
        continue
    else:
        print n,' ',m/n
        if m%n==0 and isprime(m/n):
            print "Result=%s" % (m/n)
            break
    n+=2
