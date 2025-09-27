import sys
input = sys.stdin.readline

isbn = input().strip()
sum = 0
damage = -1

for i, unit in enumerate(isbn[:-1]):
    if unit == '*':
        if i % 2 == 0:
            damage = 0
        else:
            damage = 1
        continue
    u = int(unit)
    if i % 2 == 0:
        sum += u
    else:
        sum += u * 3

if damage == -1:
    print(10 - sum%10)
elif damage == 0:
    print(10-(sum+int(isbn[-1]))%10)
else:
    print((3*(sum+int(isbn[-1]))%10)%10)