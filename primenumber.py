# N = int(input())
# # sum = [[None] *3]* N
# sum = [[0,0,0],[0,0,0]]
# for i in range(0,N):
#     print(sum[i])
# con1 = 0
# con2 = 0
# con3 = 0
# print("\n")
#
# for i in range(0,3):
#     for j in range(0,N):
#         print(i,j,end= "_ ")
#     print("\n")
#
# sum[0][0] = 23
# print(sum[0][0])
#
# for i in range(0,N):
#     print(sum[i])
# print("\n")
#-----------------------
# for i in range(0,N):
#     for j in range(0,1):
#         con1 = con1 + sum[i][j]
# print("Con1:",con1, end="")
# # print("\n")
# for i in range(0,N):
#     for j in range(1,2):
#         con2 = con2 + sum[i][j]
# print("Con2:",con2, end="")
# # print("\n")
# for i in range(0,N):
#     for j in range(2,3):
#         con3 = con3 + sum[i][j]
# print("Con3:",con3, end="")
# print("\n")


#
# for i in range(0,N):
#     for j in range(0,3):
#         sum[i][j] = list(map(int, input().split()))
#
# for x in range(0,N):
#
#



# sum = [[1,2,3],
#        [2,3,4],
#        [3,3,4],
#        [2,3,4]]
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# sum = []
# for i in range(0,N):
#     sum.append(a[i] + b[i] + c[i])
# count = 0
# for x in range(0,3):
#     if(sum[i] == 0):
#         count +=1
# if count == 3:
#     print("Yes")
# else:
#     print("No")
#-----------------------------
# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# print(a)
#---------------------------
# n = int(input())
# a = []
# for i in range(0,n):
#     a.append([0] *3)
#----------------------------
#
# n = int(input())
# a = [[0] * 3 for i in range(n)]
# print(a)
# #===============================