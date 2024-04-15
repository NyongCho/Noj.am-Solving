import sys
input = sys.stdin.readlines
output = sys.stdout.write


l = input()

for s in l:
    for e in s:
        if e == 'e':
            output('i')
        elif e == 'i':
            output('e')
        elif e == 'E':
            output('I')
        elif e == 'I':
            output('E')
        else:
            output(e)