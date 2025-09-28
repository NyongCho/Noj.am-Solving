import sys
input = sys.stdin.readline

nums = list(map(int ,input().strip().split(' ')))

def addition(a:int, b:int) -> int:
    global nums
    return nums[a]+nums[b]

def product(a:int, b:int) -> int:
    global nums
    return nums[a]*nums[b]

if nums[0] == addition(1, 2) or nums[1] == addition(0, 2) or nums[2] == addition(1, 0):
    print(1)
elif nums[0] == product(1, 2) or nums[1] == product(0, 2) or nums[2] == product(1, 0):
    print(2)
else:
    print(3)