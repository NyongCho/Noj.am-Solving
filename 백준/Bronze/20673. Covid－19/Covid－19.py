import sys
input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())

# white : avg <= 50, 2weeks <= 10
# Red   : avg >  50, 2weeks >  30

if a <= 50 and b <= 10:
    print("White")
elif b > 30:
    print("Red")
else:
    print("Yellow")