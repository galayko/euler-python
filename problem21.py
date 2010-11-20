#!/usr/bin/env python
# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
# are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def sum_divisors(a):
    l = []
    for i in xrange(1, 1+a/2):
        if a % i == 0:
            l.append(i)
    return sum(l)


amicable = {}
for i in xrange(1, 10001):
    sm = sum_divisors(i)
    if i != sm:
        tmp = sum_divisors(sm)
        if tmp==i:
            amicable[tmp] = 1
            amicable[sm] = 1
    print i
cnt = 0
for k, v in amicable.iteritems():
    cnt += k
print "Cnt=", cnt
