import sys

input = sys.stdin.readline
output = sys.stdout.write

count_win = 0

for _ in range(6):
    R = input().strip()
    if R == 'W':
        count_win += 1

if count_win >= 5:
    output('1\n')
elif count_win >= 3:
    output('2\n')
elif count_win >= 1:
    output('3\n')
else:
    output('-1\n')