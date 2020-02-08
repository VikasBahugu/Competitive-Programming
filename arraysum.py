#Filter
# a = [2,3,4,5,6,7]
# def is_greater_3(num):
#     return num>3
# b = list(filter(is_greater_3, a))
# print(b)

#Reduce
from functools import reduce
a = [2,3,4,5]
ca = reduce(lambda x,y:x+y, a)
print(ca)

# num = 0
# for i in a:
#     num = num + i
# print(num)