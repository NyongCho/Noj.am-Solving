import sys
import copy
input = sys.stdin.readline

a = [-1, -1, -1, -1]
for i in range(4):
    a[i] = int(input().strip())

f = 0
for i in range(4):
    if a[i] == a[i-1]:
        f = 1

if a[0] == a[1] == a[2] == a[3]:
    print('Fish At Constant Depth')
else:
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    b.sort()
    c.sort(reverse=True)

    if a == b and f == 0:
        print('Fish Rising')
    elif a== c and f == 0:
        print('Fish Diving')
    else:
        print('No Fish')