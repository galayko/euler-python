#!/usr/bin/env python
"""
If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

dig = ('','one','two','three','four','five','six','seven','eight','nine')
dig10 = ('','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
dig1020 = ('ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
pow = ('','thousand', 'million')

def three_digits_say(n):
    out = ''
    if n>99:
        out+=dig[n/100]+' hundred '
        if n%100>0: out+=' and '
        n=n%100
    if n>9:
        if n>19:
            out+=dig10[n/10]
        else:
            out+=dig1020[n%10]
            return out
        n=n%10
    out+=' '+dig[n]
    return out

def to_say(numb):
    out = ''
    n = numb
    for i in range(len(pow)):
        j=len(pow)-i-1
        rest = n/(10**(j*3))
        n = n%(10**(j*3))
        if rest!=0:
            out+=three_digits_say(rest)+' '+pow[j]
            if n>0: out+=' and '
    return out

def count_letter(s):
    cnt = 0
    for char in s:
        if char!=' ': cnt+=1
    return cnt

res = 0
for i in range(1,1001):
    res+=count_letter(to_say(i))
print "Res=", res
