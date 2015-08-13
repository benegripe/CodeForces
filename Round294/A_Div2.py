#http://codeforces.com/contest/519/problem/A
#solved by Benegripe
#!/usr/bin/python

white = {'Q': 9,'R': 5,'B': 3,'N': 3,'P': 1,'K': 0,'.': 0}
black = {'q': 9,'r': 5,'b': 3,'n': 3,'p': 1,'k': 0,'.': 0}
PW = 0
PB = 0
for x in range(0,8):
	s = raw_input()
	for y in s:
		if y.islower():
			PB += black[y]
		else:
			PW += white[y]

if (PW > PB):
	print "White"
elif (PW < PB):
	print "Black"
else:
	print "Draw"

