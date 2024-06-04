import sys
input = sys.stdin.readline

p, w = map(int, input().strip().split())
string = input().strip()

time = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]
group = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7]
total = 0

for i in range(len(string)):
    if string[i] == ' ':
        total += p
        continue
    if i != 0 and string[i-1] != ' ' and group[ord(string[i-1])-65] == group[ord(string[i])-65]:
        total += w
    total += time[(ord(string[i])-ord('A'))] * p

print(total)