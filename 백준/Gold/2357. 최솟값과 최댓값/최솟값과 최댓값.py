import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = []

for _ in range(N):
    t = int(input().strip())
    nums.append(t)

sn = 262144
st = [[0,float('inf')] for _ in range(sn)]

def make_segtree(start, end, idx, st):
    if start == end:
        st[idx] = [nums[start], nums[start]]
        return st[idx]
    mid = (start+end)//2
    
    c10, c11 = make_segtree(start, mid, idx*2, st)
    c20, c21 = make_segtree(mid+1, end, idx*2 + 1, st)
    if c10 > c20:
        st[idx][0] = c10
    else:
        st[idx][0] = c20

    if c11 < c21:
        st[idx][1] = c11
    else:
        st[idx][1] = c21

    return st[idx]

def find_value(start, end, idx, left, right, st):
    if end < left or right < start:
        return [0, float('inf')]
    if left <= start and end <= right:
        return st[idx]
    
    mid = (start+end) // 2
    
    c10, c11 = find_value(start, mid, idx*2, left, right, st)
    c20, c21 = find_value(mid+1, end, idx*2 + 1, left, right, st)
    r1 = 0
    r2 = 0
    if c10 > c20:
        r1 = c10
    else:
        r1 = c20

    if c11 < c21:
        r2 = c11
    else:
        r2 = c21

    return [r1, r2]


make_segtree(0, N-1, 1, st)

for _ in range(M):
    a, b = map(int, input().strip().split())
    r2, r1 = find_value(0, N-1, 1, a-1, b-1, st)
    print(r1, r2)