import sys
input = sys.stdin.readline

k,d,a = map(int, input().strip().split('/'))

ks = k+a

if ks < d or d ==0:
    print('hasu')
else:
    print('gosu')