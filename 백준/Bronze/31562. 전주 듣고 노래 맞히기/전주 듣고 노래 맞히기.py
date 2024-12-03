import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

song_list = []
for _ in range(N):
    raw = input().strip().split()

    title = raw[1]
    note = raw[2:]

    song_list.append([title, note])

for _ in range(M):
    test = list(input().strip().split())
    
    ans = None
    cnt = 0
    for i in range(N):
        if song_list[i][1][:3] == test:
            cnt += 1
            if cnt > 1:
                cnt = -1
                break
            ans = song_list[i][0]

    if cnt == 0:
        print('!')
    elif cnt == -1:
        print('?')
    else:
        print(ans)