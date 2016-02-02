#http://codeforces.com/contest/598/problem/A
#solved by Benegripe
#!/usr/bin/py

n = int(raw_input())
for i in range(1,n+1):
    res = -1
    t = int(raw_input())
    if (0 == t % 2):
        res = (1 + t)*t/2
    else:
        res = (1 + (t-1))*(t-1)/2
    print res
    while (t > 0 and  0 == t % 2):
        t -= 1
    print t
    res -= 2*t
    print res
