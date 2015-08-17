#http://codeforces.com/contest/556/problem/A
#solved by Benegripe
#!/usr/bin/python
n = int(raw_input())
s = raw_input()
zero = s.count('0')
one = s.count('1')
print n - 2*min(zero,one)
