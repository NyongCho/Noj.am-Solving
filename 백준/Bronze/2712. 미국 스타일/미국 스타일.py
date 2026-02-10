import sys
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for _ in range(T):
    N, unit = input().strip().split(" ")
    N = float(N)

    if unit == "kg":
        output(f"{N * 2.2046:0.4f} lb\n")
    elif unit == "lb":
        output(f"{N * 0.4536:0.4f} kg\n")
    elif unit == "l":
        output(f"{N * 0.2642:0.4f} g\n")
    elif unit == "g":
        output(f"{N * 3.7854:0.4f} l\n")