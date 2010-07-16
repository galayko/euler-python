#!/usr/bin/env python
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

def isprime(num):
    tmp = 2
    while tmp<num:
        if num%tmp==0:
            return False
        tmp+=1
    return True


def GetPrimeMultipliers(prod):
    templist = []
    acc = prod
    prime = 2
    while prime<=prod and acc>1:
        if acc%prime==0:
            acc = acc/prime
            templist.append(prime)
        else:
            prime+=1
            while not isprime(prime): prime+=1
    return templist

# here by list of mist of multipliers
# number 1 is skiping
multipliers = {}
number = 2
# Factorization numbers from 2 to 20
while number<=20:
     multipliers[number] = GetPrimeMultipliers(number)
     number+=1
multiplierscount = {}
for mult,lst in multipliers.iteritems():
    templist = {}
    # Counting prime numbers
    for numbers in lst:
        if not numbers in templist: templist[numbers] = 0
        templist[numbers]+=1
    # Getting a maximum prime counts
    for n,cnt in templist.iteritems():
        if not n in multiplierscount: multiplierscount[n] = 0
        if multiplierscount[n]<cnt: multiplierscount[n] = cnt
res = 1
for n,cnt in  multiplierscount.iteritems():
    res*=(n**cnt)
print 'Result=',res
