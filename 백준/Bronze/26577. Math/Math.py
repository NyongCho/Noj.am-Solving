import sys
from collections import deque
input = sys.stdin.readline

def cal_prior(c):
    if c == '*' or c =='/' or c == '%':
        return 1
    elif c == '+' or c == '-':
        return 2
    
def op(a, b, o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    elif o == '/':
        return a//b
    elif o == '%':
        return a%b

t = int(input())
oper = ['+', '-', '*', '/', '%']

while t:
    t -= 1

    formula = list(input().strip().split())
    
    stack = deque()

    form = []
    for c in formula:
        if c in oper:
            while stack and cal_prior(stack[-1]) <= cal_prior(c):
                form.append(stack.pop())
            stack.append(c)
        else:
            form.append(c)
    while stack:
        form.append(stack.pop())

    for n in form:
        if n not in oper:
            stack.append(int(n))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(op(a,b,n))
    
    print(stack.pop())