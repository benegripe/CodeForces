#http://codeforces.com/contest/520/problem/A
#solved by Benegripe
#!/usr/bin/python
n = int(raw_input())
s = raw_input()
alpha= set()
for x in s:
	if x.lower() not in alpha:
		alpha.add(x.lower())

if (26 == len(alpha)):
	print "YES"
else:
	print "NO"

	
