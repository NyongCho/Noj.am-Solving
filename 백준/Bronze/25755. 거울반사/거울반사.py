import sys
input = sys.stdin.readline

W, N = input().strip().split(' ')
N = int(N)

reflected_number = {
    1:1,
    2:5,
    3:'?',
    4:'?',
    5:2,
    6:'?',
    7:'?',
    8:8,
    9:'?'
}

num = [list(map(int, input().strip().split(' '))) for _ in range(N)]

i_start, i_end, j_start, j_end = 0, N, 0, N
i_step, j_step = 1, 1

if W == 'D' or W == 'U':
    i_start = N - 1
    i_end = -1
    i_step = -1
elif W == 'L' or W == 'R':
    j_start = N - 1
    j_end = -1
    j_step = -1

for i in range(i_start, i_end, i_step):
    for j in range(j_start, j_end, j_step):
        print(reflected_number[num[i][j]], end=" ")
    print()