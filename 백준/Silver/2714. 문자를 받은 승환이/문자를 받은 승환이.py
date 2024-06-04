import sys
input = sys.stdin.readline

def str2int(l):
    result = 0
    for i, e in enumerate(reversed(l)):
        result += 2**i * int(e)
    return result


n = int(input().strip())

for _ in range(n):
    r, c, x = input().strip().split()
    r = int(r)
    c = int(c)
    x = x.strip()
    m = []
    idx = 0
    for i in range(r):
        t = []
        for j in range(c):
            t.append(x[idx])
            idx += 1
        m.append(t)

    chr_cnt = 0
    s_x = -1
    s_y = 1
    C = []
    result =[]

    if r == 1 or c == 1:
        for i in range(max(c,r)):
            C.append(x[i])   
            chr_cnt += 1
            if chr_cnt == 5:
                result.append(C)
                C = []
                chr_cnt = 0
    else:
        for i in range(c):
            C.append(m[0][i])
            chr_cnt += 1
            if chr_cnt == 5:
                result.append(C)
                C = []
                chr_cnt = 0
        rot = 0
        if r >= c:
            rot = c
        else:
            rot = r-1
        x = c-1
        y = 0
        r -= 1
        c -= 1
        for _ in range(rot):
            for i in range(r):
                y += s_y
                C.append(m[y][x])
                chr_cnt += 1
                if chr_cnt == 5:
                    result.append(C)
                    C = []
                    chr_cnt = 0
            r -= 1
            s_y *= -1
            
            for _ in range(c):
                x += s_x
                C.append(m[y][x])
                chr_cnt += 1
                if chr_cnt == 5:
                    result.append(C)
                    C = []
                    chr_cnt = 0

            c -= 1
            s_x *= -1
    if len(C) != 0:
        tmp = len(C)
        for _ in range(5-tmp):
            C.append('0')
        if '1' in C:
            result.append(C)

    text = ""
    for l in result:
        plus = str2int(l)
        if plus == 0:
            text += ' '
        else:
            text += chr(64+plus)

    print(text.strip())