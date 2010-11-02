#!/usr/bin/env python
# Starting in the top left corner of a 2x2 grid, there are 6 routes
# (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

# Solution note:
# Sorry, but this promlem is easy.
# We coding direction:
#    0 - down
#    1 - right
# So, route in NxN grid is 2*N bit-value and in this value N zeroes.
# Number of permutations (m,n) is:
# n!/(m! (n-m)!)
# In out case m=n/2, so
# Routes count is: (N*2)!/N!^2

def fact(n):
    res = 1
    for i in range(1,n+1): res*=i
    return res

n=20
res = fact(n*2)/(fact(n)**2)
print "Res=", res
