import sys
input = sys.stdin.readline

x = input().strip()

l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(8):
    if l[i] in x:
        x = x.replace(l[i], "0")
print(len(x))