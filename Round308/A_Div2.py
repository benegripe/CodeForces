#http://codeforces.com/contest/552/problem/A
#solved by Benegripe
#!/usr/bin/python

n = int(raw_input())
m = [[0 for x in range(102)] for x in range(102)]
for x in range(0,n):
	x1,y1,x2,y2 = raw_input().split(' ')
	for y in range(int(x1),int(x2)+1):
		for w in range(int(y1),int(y2)+1):
			m[y][w] +=1	

s = 0
for y in range(1,101):
	for w in range(1,101):
		s+= m[y][w] 
print s


