import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0

    def T(n):
        if n == 1:
            return 1
        return T(n - 1) + n

    for k in range(1, n+1):
        ans += k * T(k + 1)

    print(ans)