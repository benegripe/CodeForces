#http://codeforces.com/contest/519/problem/B
#problem solved by Benegripe
#/usr/bin/py
error = {}
n = int(raw_input())
j = 0
for i in raw_input().split():
	error [i] = error.get(i,0) + 1
	j += 1

first = dict(error)
second = dict(error)

for i in raw_input().split():
	first[i] = first.get(i,0) - 1

for key in first:
	if first[key] != 0:
			print key
			second[key] -= 1
			break

for i in raw_input().split():
	second[i] = second.get(i,0) - 1
for key in second:
	if second[key] != 0:
			print key
			break
