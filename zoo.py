str = list(input())
countz = 0
for item in str:
    if item == 'z':
        countz += 1

countz = countz * 2
counto = 0
for item in str:
    if item == 'o':
        counto += 1
if countz == counto:
    print("YES")
else:
    print("NO")
