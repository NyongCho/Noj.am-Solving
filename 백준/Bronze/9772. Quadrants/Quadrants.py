import sys
input = sys.stdin.readline

while True:
    a, b = input().strip().split()
    a = float(a)
    b = float(b)
    if a == 0 or b == 0:
        print("AXIS")
        if a == b:
            break
        continue
    
    if b > 0:
        if a > 0:
            print("Q1")
        else:
            print("Q2")
    else:
        if a > 0:
            print("Q4")
        else:
            print("Q3")        
            