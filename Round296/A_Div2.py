#http://codeforces.com/contest/527/problem/A
#solved by Benegripe
#!/usr/bin/python
z = raw_input().split(' ')
a = int(z[0])
b = int(z[1])
square = 0
while (a != b) and (0 != b): 
	square += a/b
	c = a % b
	d = min(a,b)
	a = max(d,c)
	b = min(d,c)
print square
	
