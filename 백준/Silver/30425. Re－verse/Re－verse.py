import sys
input = sys.stdin.readline

n = int(input())

string = input().rstrip()
new = string
cnt = 1
p = 0

for i in range(1, n):
    # print(f"{i} : {new[i:], string[:n - i - p]} - {new}")
    if new[i:] == string[:n - i - p]:
        new = new[:i] + string
        p = n-i
        cnt += 1

print(cnt)
# print(new)