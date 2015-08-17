#http://codeforces.com/contest/525/problem/A
#solved by Benegripe
#!/usr/bin/python

n = int(raw_input())
s = raw_input()
key = {}
for x in range(97,123):
	key[chr(x)] = 0
buy = 0
for x in range(0,len(s)-1):
	if 0 == x % 2:
		if s[x] != s[x+1].lower():
			key[s[x]] += 1
			if key[s[x+1].lower()] > 0:
					key[s[x+1].lower()] -= 1
			else:
					buy += 1
print buy
