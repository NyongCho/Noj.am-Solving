import math

def solution(signals):
    n = len(signals)
    lengths = []
    arr = []
    for signal in signals:
        lengths.append(sum(signal))
        tmp = signal[0]*[0]+signal[1]*[1]+signal[2]*[0]
        arr.append(tmp)
        
    f = math.lcm(*lengths)
    
    fl = [0 for _ in range(f)]
    
    for i in range(n):
        l = len(arr[i])
        a = f // l
        for j in range(a):
            for k in range(l):
                fl[j*l+k] += arr[i][k]
                
    answer = -1
                
    for x in range(f):
        if fl[x] == n:
            answer = x+1
            break
            
    return answer