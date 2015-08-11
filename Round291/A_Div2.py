#http://codeforces.com/contest/514/problem/A
#solved by Benegripe
#!/usr/bin/python
s = 0
for x in raw_input():
	if int(x) <= 4 :
		s = 10*s + int(x)
	elif 0 == s and int(x) == 9:
		s = 10*s + int(x)
	else:
		s = 10*s + int(9-int(x))
print s
