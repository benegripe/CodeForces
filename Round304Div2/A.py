#http://codeforces.com/contest/546/problem/A
#problem solved by Benegripe with python 2.7
#!/usr/bin/python

k,n,w = raw_input().split()
cost = ( (int(k) + int(w)*int(k))*int(w) ) / 2
if (cost > int(n)):
	print (cost - int(n))
else:
	print "0"
