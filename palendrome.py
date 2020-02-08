# str = list(input())
# lst = []
#
# for i in range(0,len(str)):
#     # print(str[i], end=" ")
#     lst.append(str[i])
# lst.reverse()
# count = 0
# for i in range(0, len(lst)):
#     if lst[i] == str[i]:
#         count += 1
#
#         # print(count)
# if count == len(str):
#     print("YES")
# else:
#     print("NO")

x = list(input())
ls = []

for k in range(0, len(x)):
    ls.append(x[k])
ls.reverse()

for i in range(0,len(x)):
    if x[i] == ls[i]:
        count += 1
if count == len(x):
    print("YES")
else:
    print("NO")