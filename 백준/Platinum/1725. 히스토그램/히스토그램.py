import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input().strip())
nums = []

for _ in range(N):
    t = int(input().strip())
    nums.append(t)

sn = 262144
st = [0 for _ in range(sn)]

def minimum(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    if nums[a] > nums[b]:
        return b
    else:
        return a

def make_segtree(start, end, idx, st):
    if start == end:
        st[idx] = start
        return start
    mid = (start+end)//2
    
    left_min_idx = make_segtree(start, mid, idx*2, st)
    right_min_idx = make_segtree(mid+1, end, idx*2 + 1, st)

    st[idx] = minimum(left_min_idx, right_min_idx)

    return st[idx]

def find_value(start, end, idx, left, right, st):
    if end < left or right < start:
        return -1
    if left <= start and end <= right:
        return st[idx]
    
    mid = (start+end) // 2
    
    left_min_idx = find_value(start, mid, idx*2, left, right, st)
    right_min_idx = find_value(mid+1, end, idx*2 + 1, left, right, st)

    return minimum(left_min_idx, right_min_idx)

def divide(start, end):
    min_idx = find_value(0, N-1, 1, start, end, st)
    area = nums[min_idx] * (end-start + 1)

    left = right = 0
    if start < min_idx:
        left = divide(start, min_idx-1)
    if end > min_idx:
        right = divide(min_idx+1, end)
    return max(area, max(left, right))
    

make_segtree(0, N-1, 1, st)
print(divide(0, N-1))