inp = list(map(int,input().split()))
count = 0
for i in range(inp[0],inp[1]+1):
    if i%inp[2] == 0:
        count += 1
print(count)