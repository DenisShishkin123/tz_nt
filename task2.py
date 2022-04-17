with open(input(), encoding='utf-8')  as file1, open(input(), encoding='utf-8') as file2:
    x1, y1 = map(float, file1.readline().split())
    r = float(file1.readline())
    l = list(map(lambda x: x.strip(), file2.readlines()))

for i in l:
    x2, y2 = map(float, i.split())
    res = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if res > r:
        print(2)
    elif res == r:
        print(0)
    elif res < r:
        print(1)