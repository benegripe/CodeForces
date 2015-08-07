#http://codeforces.com/contest/544/problem/A
#solved by Benegripe with python 2.7
#!/usr/bin/python

k = int(raw_input())
begin = set()
beautiful = []
q = raw_input()
s = q[0]
begin.add(q[0])
for x in range(1,len(q)):
	if q[x] not in begin:
			beautiful.append(s)
			begin.add(q[x])
			s = q[x]
	else:
			s += q[x]
beautiful.append(s)

if len(beautiful) < k:
	print "NO"
else:
	print "YES"
	for x in range(0,k-1):
		print beautiful[x]	
	s = ''
	for x in range(k-1,len(beautiful)):
			s += beautiful[x]
	print s
