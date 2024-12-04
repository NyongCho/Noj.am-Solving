import sys
input = sys.stdin.readline

n = int(input())
cnt = -1
sentence = []

digit_0 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
digit_1 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
digit_2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"

for _ in range(n):
    sentence.append(input().rstrip())
    cnt += len(sentence[-1])

ans = ""

for num in range(cnt, 1000):
    text = ""
    a = num//100
    b = (num%100)//10
    c = num%10
    if a != 0:
        text += digit_0[a-1] + hundred
    if b != 0:
        if b == 1:
            if c != 0:
                text += digit_1[c-1]
            else:
                text += digit_0[9]
        else:
            text += digit_2[b-2]
            if c != 0: 
                text += digit_0[c-1]
    else:   
        if c != 0:
            text += digit_0[c-1]

    
    length = len(text)
    # print(text, num)
    # print(f"[{cnt} + {length} = {cnt + length}_{num}] - {text}")
    if length + cnt == num and num != 0:
        ans = text
        break

for i in range(len(sentence)):
    if sentence[i] == '$':
        sentence[i] = ans
        break

print(' '.join(sentence))