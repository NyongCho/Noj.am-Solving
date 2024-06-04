import sys
input = sys.stdin.readline

a = list(input().strip())
l = []
x = 0
for i in a:
    if i != '-' and i != '+':
        x *= 10
        x += int(i)
    else:
        l.append(x)
        x = 0
        l.append(i)
l.append(x)
#print(l)

c = []
i = 0
len = len(l)
while i < len:
    if l[i] == '+':
        l[i+1] = (l[i-1]+l[i+1])
        i+=1
    elif l[i] == '-':
        c.append(-1*l[i-1])
    i+=1
c.append(-1*l[-1])
c[0] *= -1
#print(c)
print(sum(c))