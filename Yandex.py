b = input()
x = []
nado = []
count = 0
check = set()
a = input()
ax = a.split(' ... ')
aa = a.lower().split(' ... ')
for i in b.lower():
    x.append(i)
for j in range(len(aa)):
    for k in aa[j]:
        if k in x:
            count += 1
            if k in check:
                count -= 1
            check.add(k)
    if count > 4:
        nado.append(ax[j])
    count = 0
    check = set()
print(*nado, sep=' * ')