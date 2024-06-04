import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = n
for i in range(n):
    arr = input().strip().split()
    h = [0 for _ in range(26)]
    for j in range(len(arr[0])):
        t = ord(arr[0][j])
        if h[t-97] == 0:
            h[t-97] = 1
        elif h[t-97] == 1:
            if arr[0][j-1] != arr[0][j]:
                cnt -= 1
                break
       
print(cnt)