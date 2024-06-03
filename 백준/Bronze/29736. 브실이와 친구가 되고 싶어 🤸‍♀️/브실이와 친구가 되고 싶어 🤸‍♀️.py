import sys
input = sys.stdin.readline

a, b = map(int , input().strip().split())
k, x = map(int , input().strip().split())
cnt = 0

for i in range(a,b+1):
	if k-x <= i <= k+x:
		cnt += 1

if not cnt:
	print("IMPOSSIBLE")
else:
	print(cnt)