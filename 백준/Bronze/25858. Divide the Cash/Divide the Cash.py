import sys
input = sys.stdin.readline
output = sys.stdout.write

n, d = map(int, input().strip().split())

total_solved = 0
students_solved = []

for _ in range(n):
    students_solved.append(int(input().strip()))
    total_solved += students_solved[-1]

for i in range(n):
    output(f'{d*students_solved[i]//total_solved}\n')