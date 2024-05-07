import sys
input = sys.stdin.readline

r = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
for i in range(3):
    n = int(input())
    if i % 2 == 1:
        n *= 3
    r += n

print(f"The 1-3-sum is {r}")