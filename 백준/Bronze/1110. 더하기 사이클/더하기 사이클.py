n = int(input())
f = 0
m = n
while(m != n or f == 0):
	f += 1
	m = (m%10)*10 + (m//10 + m%10)%10

print(f,end="")