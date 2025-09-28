import sys
input = sys.stdin.readline

n = int(input())
halls = input().strip()

hands_on_coffee = 0
attended_lectures = 0

for lecture in halls:
    if lecture == '1':
        attended_lectures += 1
        hands_on_coffee = 2
    else:
        if hands_on_coffee > 0:
            attended_lectures += 1
            hands_on_coffee -= 1

print(attended_lectures)