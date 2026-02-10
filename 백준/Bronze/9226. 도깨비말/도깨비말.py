import sys

input = sys.stdin.readline
output = sys.stdout.write

momum = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input().strip()
    if word == "#":
        break
    
    result = ""

    for i, u in enumerate(word):
        if u in momum:
            result = word[i:] + word[:i] + "ay\n"
            break

    if result == "":
        output(word + "ay\n")
    else:
        output(f'{result}')
