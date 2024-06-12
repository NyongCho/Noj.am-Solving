from collections import deque

def solution(s):
    st = deque()
    f = 0
    for e in s:
        if e == '(':
            st.append(e)
        elif e == ')':
            if not st:
                f = 1
                break
            st.pop()
        
    if f or st:
        return False
    else:
        return True