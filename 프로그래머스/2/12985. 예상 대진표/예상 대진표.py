def solution(n,a,b):
    answer = 0
    
    x = a
    y = b
    
    while x != y:
        x = int(x/2+0.5)
        y = int(y/2+0.5)
        answer += 1

    return answer