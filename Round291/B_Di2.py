#http://codeforces.com/contest/514/problem/B
#solved by Benegripe
#!/usr/bin/py

n,x,y = [int(x) for x in raw_input().split()]
times = {}
for i in range(n):
	x0,y0 = [int(z) for z in raw_input().split()]
	if  0 == x-x0:
		cf = float('inf')
	else:
		cf = float(y0-y)/(x0-x)
	times[cf] = times.get(cf,0) + 1
print len(times)
