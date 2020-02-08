tc = int(input())
ca = []
cb = []
a = [0,0]
for i in range(0,tc):
    a.append(input().split())
    ca[i].append(a[0])
    cb[i].append(a[1])

    # a = ca[i]
    # b = cb[i]
    # for item in a:
    #     print(item)
print(ca,"__",cb)