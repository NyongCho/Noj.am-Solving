import sys
input = sys.stdin.readline

def reve(a):
    return a[::-1]

a = input().strip()

cnt = 0
f = 0
for i, e in enumerate(a):
    if e == '<':
        sys.stdout.write(reve(a[i-cnt:i])+e)
        cnt = 0
        f = 1
    elif e == '>':
        sys.stdout.write(e)
        f = 0
    elif f == 0 and e == ' ':
        sys.stdout.write(reve(a[i-cnt:i])+' ')
        cnt = 0
        continue
    elif f == 1:
        sys.stdout.write(e)
    else:
        cnt += 1

if a[-1] != '>':
    sys.stdout.write(reve(a[len(a)-cnt:len(a)]))