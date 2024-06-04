import sys
input = sys.stdin.readline

n = int(input().strip())

a = input().strip()
cnt = 0
total = 0
n_cnt = 0
while True:
    if a == '':
        t = (total-cnt)/total*100
        t = int((t*10+0.5))/10
        if t == int(t):
            print(f"Efficiency ratio is {int(t)}%.")
        else:
            print("Efficiency ratio is {:.1f}%.".format(t))
            
        cnt = 0
        total = 0
        n_cnt += 1
        if n == n_cnt:
            break

    total += len(a)
    cnt += a.count('#')
    a = input().strip()