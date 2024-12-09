import sys
from sys import stdin
from sys import stdout

n, m, b = map(int, stdin.readline().split())
dict={}
for _ in range(n):
    for i in map(int, stdin.readline().split()):
        if(dict.get(i) == None):
            dict[i] = 1
        else:
            dict[i] += 1
mx = max(dict.keys())
mn = min(dict.keys())
min_time= sys.maxsize
a_block = 0

for p in range(mn,mx+1):
    need_block = 0
    time = 0
    for q,z in dict.items():
        tmp = p - q
        need_block += tmp*dict[q]
        time += tmp*dict[q] if tmp >= 0 else tmp*dict[q]*-2

    if(need_block <= b):
        if(min_time >= time):
            min_time = time
            a_block = p

stdout.write(str(min_time)+" "+str(a_block))