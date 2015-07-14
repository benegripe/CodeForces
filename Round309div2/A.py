#http://codeforces.com/contest/551/problem/A
#Problem solved by Benegripe with Python 2.7

#!/usr/bin/python

s = raw_input();
sol = 26*(len(s)+1);
sol -= len(s);
print sol
