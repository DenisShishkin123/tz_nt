n, m = map(int, input().split())
k = 1
while True:
    print(k, end='')
    k = 1 + (k + m - 2) % n
    if k == 1:
        break    
print()