#http://codeforces.com/contest/520/problem/B
#problem solved by Benegripe
#/usr/bin/py
n,m = [int(x) for x in raw_input().split()]
if n > m :
	print (n-m)
elif n < m:
	sol = 0
	while n < m:
		if 1 == m % 2:
			sol += 1
			m += 1
		else:
			m /= 2
			sol += 1
	if n != m:
		sol += n - m
	print (sol)
