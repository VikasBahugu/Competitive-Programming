#Remove Duplicate element without affecting the order.
# a = [2,1,4,1]
# a = list(dict.fromkeys(a))
# print(a)
#where set method does it and sort them.
t = int(input())+1
ls =  list(map(int,str(t)))
a = list(dict.fromkeys(ls))
while a != ls:
    t += 1
    ls = list(map(int, str(t)))
    a = list(dict.fromkeys(ls))
a=int("".join(map(str,a)))
print(a)



# # t=1987
# # lis = []
# # lis = list(map(int,str(t)))
# # print(lis)
