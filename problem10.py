#!/usr/bin/env python
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

summ=0
maxnumber = 2000000
arr = {}
i=2
# Fill a sieve of Eratosthenes
# It's bad for big numbers, but I don't know better method
while i<maxnumber:
    arr[i]=1
    i+=1
i=2
while i<len(arr):
    try:
        del arr[i]
        summ+=i
    except:
        pass
    j=i*2
    while j<maxnumber:
        try:
            del arr[j]
        except:
            pass
        j+=i
    print "i=",i
    i+=1
    while (i<len(arr)) and (i not in arr): i+=1
summ+=sum(arr.keys())
print "Res=", summ
