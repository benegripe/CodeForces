#http://codeforces.com/contest/515/problem/A
#problem solved by Benegripe
#!/usr/bin/python

a,b,s = raw_input().split(' ')
if int(s) < abs(int(a)) + abs(int(b)):
	print "No"
elif 1 == (abs(int(a)) + abs(int(b)) - int(s)) % 2:
	print "No"
else:
	print "Yes"
	
