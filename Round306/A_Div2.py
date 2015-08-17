#http://codeforces.com/contest/550/problem/A
#problem solved by Benegripe python 2.7
#!/usr/bin/python

s = raw_input()
if s.count('AB') > 0 and s.count('BA') > 0 and (s.count('AB') + s.count('BA') - s.count('ABA') -s.count('BAB') > 1):
	print "YES"
else:
	print "NO"
