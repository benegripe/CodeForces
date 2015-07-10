#http://codeforces.com/contest/551/problem/A
#Problem solved by Benegripe with Python 2.7

#!/usr/bin/python

import  re
import sys
from array import *

n = int(raw_input())
rating = []
sol = []
a = raw_input()
rating = [int(p) for p in a.split(' ')]
for x in range(0,n):
    cont = 1
    for y in range(0,n):
        if rating[x] < rating[y]:
            cont+= 1
    sol.append(cont)

for y in sol:
    print y,
