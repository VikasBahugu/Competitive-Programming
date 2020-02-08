a = int(input())
l = []
m = []
lc = l.copy()
ls = []
for i in range(0,a):
    l = list(map(str,str(input())))
    m = list(map(str,str(input())))
    lc = l.copy()
    for item in lc:
        if item in m:
            it = item
            l.remove(it)
            m.remove(it)
    lent = len(l) + len(m)
    ls.append(lent)
for i in range(0,len(ls)):
    print(ls[i])


