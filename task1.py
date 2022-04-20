# task1
import sys

def func(n,m):
    n, m = int(n), int(m)
    l=[i for i in range(1,n+1)]*10
    res=[]
    for i in range(0,100,m-1):
        res.append(l[i])
        if l[i:i+m][-1]==1:
            return print(*res,sep='')


func(*sys.argv[1:])
