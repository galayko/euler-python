#!/usr/bin/env python
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6^(th) prime is 13.
# What is the 10001'st prime number?

maxorder = 10001
# Length of sieve of Eratosthenes array
arraylenght = maxorder*30
erato = {} # Preliminary dict of sieve of Eratosthenes
ready = [] # Array of prime numbers
for i in xrange(2, arraylenght+2):
	erato[i] = 1
i=2
while i<arraylenght:
	if erato[i]==0:
		i+=1
		continue
	j = 2
	while j*i<arraylenght:
		erato[j*i]=0
		j+=1
	i+=1
for num,item in erato.iteritems():
	if item==1: ready.append(num)
print 'Result=',ready[maxorder-1]
