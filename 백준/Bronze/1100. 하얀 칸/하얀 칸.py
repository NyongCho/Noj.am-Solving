import sys
input = sys.stdin.readline

cnt = 0
for i in range(8):
    a = list(input().strip())
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0 and a[j] == 'F':
                cnt += 1
    else:
        for j in range(8):
            if j % 2 == 1 and a[j] == 'F':
                cnt += 1

print(cnt)