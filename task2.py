# task2
import sys

def task2(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        a,b,r = map(float, f1.read().split())
        l=(f2.readlines())
        for i in l:
            x,y=list(map(float, i.split()))
            if (x - a) ** 2 + (y - b) ** 2 < r ** 2 : print(1)
            elif (x - a) ** 2 + (y - b) ** 2 == r ** 2 : print(0)
            elif (x - a) ** 2 + (y - b) ** 2 > r ** 2 : print(2)


task2(*sys.argv[1:])

