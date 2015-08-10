#http://codeforces.com/contest/540/problem/A
#solved by Benegripe
#!/usr/bin/python
n = int(raw_input())
begin = raw_input()
end = raw_input()
sol = 0
for x in range(0,n):
	sol += min( max(int(begin[x]),int(end[x])) - min(int(begin[x]),int(end[x])), 10+min(int(begin[x]),int(end[x])) - max(int(begin[x]),int(end[x])))
print sol

