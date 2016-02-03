#http://codeforces.com/contest/598/problem/A
#solved by Benegripe
#!/usr/bin/py

def sum_neg(x):
    base = 2
    while (base <= x):
        base *= 2
    base -= 1
    return -base

n = int(raw_input())
for i in range(0,n):
    t = int(raw_input())
    if (1 == t % 2):
        sol = t*(t+1)/2
    else:
        sol = t*(t-1)/2
        sol += t
    num = sum_neg(t)
    sol += 2*num
    print sol
