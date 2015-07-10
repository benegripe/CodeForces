#http://codeforces.com/contest/548/problem/A
#Problem solved by Benegripe with Python 2.7

#!/usr/bin/python
s = raw_input()
k = int(raw_input())
sol = "YES"

if 0 != len(s)%k:
	sol = "NO"
else:
	j = 0
	while (j < len(s) and sol == "YES"):
		i = 0
		while (i < (len(s)/k)/2 and sol == "YES"):
			if (s[i+j] != s[j + (len(s)/k)-i-1]):
				sol = "NO"
			i += 1
		j += len(s)/k

print sol

