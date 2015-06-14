#http://codeforces.com/contest/545/problem/B

#!/usr/bin/python

a = raw_input()
b = raw_input()
c = '' 
diff = 0
aux = 1

if len(a) != len(b) :
    print "impossible"
else:
    for x,y in zip(a,b):
        if x == y:
            c += x
        elif 1 == aux:
            c += x
            aux = 0
            diff+= 1
        else: 
            c += y
            aux = 1
            diff+= 1
if 0 == diff % 2:
    print c
else:
    print 'impossible'
