#http://codeforces.com/contest/510/problem/B
#problem solved by Benegripe
#/usr/bin/py

n,m = map(int,raw_input().split())
p = [list(raw_input()+'#') for _ in range(n)] + [list('#'*(m+1))]
cont = 1
while cont:
	cont = 0
	for x in range(n):
		for y in range(m):
			if '#' != p[x][y]:
				s = 0
				s += int(p[x][y] == p[x-1][y])
				s += int(p[x][y] == p[x+1][y])
				s += int(p[x][y] == p[x][y+1])
				s += int(p[x][y] == p[x][y-1])
				if s < 2:
					p[x][y] = '#'
					cont = 1

for x in range(n+1):
	for y in range(m+1):
		if p[x][y] != '#':
			print "Yes"
			exit(0)
print "No"	
				
