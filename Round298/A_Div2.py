#http://codeforces.com/contest/534/problem/A
#solved by Benegripe
#!/usr/bin/python

n = int(raw_input())
if (n > 3):
	print n
	for x in range(1,n+1):
		if 0 == x % 2:
			print n+1-x,
	for x in range(1,n+1):
		if 1 == x % 2:
			print n+1-x,
elif (3 == n):
		print '2'
		print '1 3'
else:
		print '1'
		print '1'

	

