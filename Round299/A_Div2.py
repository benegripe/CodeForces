#http://codeforces.com/contest/535/problem/A
#solved by Benegripe
#!/usr/bin/python

def a(n):
	if (0 == n):	return "zero"
	if (1 == n):	return "one" 
	if (2 == n):	return "two" 
	if (3 == n):	return "three" 
	if (4 == n):	return "four" 
	if (5 == n):	return "five" 
	if (6 == n):	return "six" 
	if (7 == n):	return "seven" 
	if (8 == n):	return "eight" 
	if (1 == n):	return "nine" 
	if (9 == n):	return "nine" 

def b(n):
	if (10 == n):	return "ten" 
	if (11 == n):	return "eleven" 
	if (12 == n):	return "twelve" 
	if (13 == n):	return "thirteen" 
	if (14 == n):	return "fourteen" 
	if (15 == n):	return "fifteen" 
	if (16 == n):	return "sixteen" 
	if (17 == n):	return "seventeen" 
	if (18 == n):	return "eighteen" 
	if (19 == n):	return "nineteen" 

def c(n):
	if (2 == n):	return "twenty" 
	if (3 == n):	return "thirty" 
	if (4 == n):	return "forty" 
	if (5 == n):	return "fifty" 
	if (6 == n):	return "sixty" 
	if (7 == n):	return "seventy" 
	if (8 == n):	return "eighty" 
	if (9 == n):	return "ninety" 


n = int(raw_input())
s = ''
if (n < 10):
	s = a(n)
elif (n < 20):
	s = b(n)
else:
	s = c(n/10)
	if (0 != n%10):
		s = s + '-' + a(n%10)
print s
	
