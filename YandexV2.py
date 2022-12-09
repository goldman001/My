n = int(input())
x = set()
for i in range(n):
    a = input().split()
    b = input().split()
    for j in b:
        if j not in a:
            x.add(j)
    print(*x, sep=' ')
    print(n)