# list = []
# n = int(input())
#
# for i in range(0,n):
#     x = list(map(int, i).split())
#     list.append(x

n = int(input())
lis = [1]
data = list(map(int, input().split()))
for i in data:
    if i % 6 == 0:
        lis.append(i)
print(lis)
