#http://codeforces.com/contest/515/problem/B
#problem solved by Benegripe
#/usr/bin/py
n,m = map(int,raw_input().split())
N = set(map(int,raw_input().split(' ')[1:]))
M = set(map(int,raw_input().split(' ')[1:]))
for i in range(1000000):
	if (i%n) in N or (i%m) in M:
			N.add(i%n)
			M.add(i%m)
if len(N)+len(M) == n + m:
	print "Yes"
else:
	print "No"
