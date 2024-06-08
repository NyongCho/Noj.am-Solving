import sys
input = sys.stdin.readline

t = int(input().strip())

for idx in range(t):
    n = int(input().strip())
    l = list(map(int, input().strip().split()))
    cnt = 0
    present = l[0]
    for i in range(1, len(l)):
        if l[i] > present:
            present = l[i]
        else:
            cnt += 1

    print(f"Case #{idx+1}: {cnt}")