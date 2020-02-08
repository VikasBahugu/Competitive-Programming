lst = list(input())
print(lst)
pt = [0,0]
print(pt)
for item in lst:
    if item == "L":
        pt[0] = pt[0] - 1
    elif item == "R":
        pt[0] = pt[0] + 1
    elif item == "U":
        pt[1] = pt[1] + 1
    else: #for "D"
        pt[1] = pt[1] - 1

print(pt[0],pt[1])