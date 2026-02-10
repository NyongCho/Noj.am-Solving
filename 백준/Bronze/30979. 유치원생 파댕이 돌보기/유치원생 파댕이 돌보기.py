import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input())
N = int(input())
arr = list(map(int, input().split()))
sum_arr = sum(arr)

if T <= sum_arr:
    output("Padaeng_i Happy")
else:
    output("Padaeng_i Cry")