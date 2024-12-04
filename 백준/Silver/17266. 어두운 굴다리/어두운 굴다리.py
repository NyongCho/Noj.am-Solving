import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int,input().split()))
# print(lights)

max_diff = max(lights[0], abs(lights[-1] - N))

for i in range(len(lights) - 1):
    diff = int(abs(lights[i] - lights[i + 1])/2.0 + 0.5)
    # print(i, lights[i])
    if max_diff < diff:
        max_diff = diff
        
print(max_diff)