import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if(s == '#'):
        break
    else:
        cnt = 0
        for i in s:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                cnt += 1
        sys.stdout.write(str(cnt)+"\n")