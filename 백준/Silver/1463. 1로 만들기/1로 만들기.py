n = int(input())
l = [10000]*1000001
l[1], l[2], l[3] = 0, 1, 1
i = 4

while i <= n:
	l[i] = l[i-1] + 1
	if i%2 == 0:
		l[i] = (l[i//2] + 1 if (l[i//2] + 1 < l[i]) else l[i])
	if i%3 == 0:
		l[i] = (l[i//3] + 1 if (l[i//3] + 1 < l[i]) else l[i])
	i+=1
print(l[n])