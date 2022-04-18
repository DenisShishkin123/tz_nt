# task1

def func(n,m):
    l=[i for i in range(1,n+1)]*10
    res=[]
    for i in range(0,100,m-1):
        res.append(l[i])
        if l[i:i+m][-1]==1:
            return print(*res,sep='')


func(*map(int, input().split()))