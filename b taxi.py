# gr = int(input())
# sc = list(map(int,input().split()))
# taxi = 0
# while(len(sc) != 0):
#     if sc[0] == 4:
#         taxi += 1
#         sc.remove(4)
#     elif sc[0] == 3:
#         sc.remove(3)
#         taxi += 1
#         if 1 in sc:
#             sc.remove(1)
#     elif sc[0] == 2:
#         sc.remove(2)
#         taxi += 1
#         if 2 in sc:
#             sc.remove(2)
#         elif 1 in sc:
#             sc.remove(1)
#             if 1 in sc:
#                 sc.remove(1)
#     elif sc[0] == 1:
#         sc.remove(1)
#         taxi += 1
#         if 3 in sc:
#             sc.remove(3)
#         elif 2 in sc:
#             sc.remove(2)
#             if 1 in sc:
#                 sc.remove(1)
#         elif 1 in sc:
#             sc.remove(1)
#             if 2 in sc:
#                 sc.remove(2)
#             elif 1 in sc:
#                 sc.remove(1)
#                 if 1 in sc:
#                     sc.remove(1)
# print(taxi)










#=====================================================
#does not work for 78th test case.
# gr = int(input())
# sc = list(map(int,input().split()))
# taxi = 0
# c = 0
# i = 1
#
# c = sc.count(4)
# taxi = taxi + c
# while(4 in sc):
#     sc.remove(4)
#
# c = sc.count(2)
# print(c)
# if c%2 == 0:
#     taxi = taxi + c/2
#     taxi = int(taxi)
# elif (c-1)%2 == 0:
#     taxi = taxi + int((c-1)/2)
# if c%2 == 0:
#     while(c != 0):
#         sc.remove(2)
#         c -= 1
# elif (c-1)%2 == 0:
#     while(c != 1):
#         sc.remove(2)
#         c -= 1
# print(c)
# c = sc.count(1)
# if c%4 == 0:
#     taxi = taxi + int(c/4)
# elif (c-1)%4 == 0:
#     taxi = taxi + int((c-1)/4)
# elif (c-2)%4 == 0:
#     taxi = taxi + int((c-2)/4)
# elif (c-3)%4 == 0:
#     taxi = taxi + int((c-3)/4)
# if c%4 == 0:
#     while(c!= 0):
#         sc.remove(1)
#         c -= 1
# elif (c-1)%4 == 0:
#     while(c!= 1):
#         sc.remove(1)
#         c -= 1
# elif (c-2)%4 == 0:
#     while(c!=2):
#         sc.remove(1)
#         c -= 1
# elif (c-3)%4 == 0:
#     while(c!=3):
#         sc.remove(1)
#         c-= 1
#
#
# while(len(sc) != 0):
#     if sc[0] == 4:
#         taxi += 1
#         sc.remove(4)
#     elif sc[0] == 3:
#         sc.remove(3)
#         taxi += 1
#         if 1 in sc:
#             sc.remove(1)
#     elif sc[0] == 2:
#         sc.remove(2)
#         taxi += 1
#         if 2 in sc:
#             sc.remove(2)
#         elif 1 in sc:
#             sc.remove(1)
#             if 1 in sc:
#                 sc.remove(1)
#     elif sc[0] == 1:
#         sc.remove(1)
#         taxi += 1
#         if 3 in sc:
#             sc.remove(3)
#         elif 2 in sc:
#             sc.remove(2)
#             if 1 in sc:
#                 sc.remove(1)
#         elif 1 in sc:
#             sc.remove(1)
#             if 2 in sc:
#                 sc.remove(2)
#             elif 1 in sc:
#                 sc.remove(1)
#                 if 1 in sc:
#                     sc.remove(1)
# print(taxi)


#-------------------------------------------------

#Workking but time limit exceeeds.
gr = int(input())
sc = []
sc = list(map(int,input().split()))[:gr]
sc.sort(reverse= True)
taxi = 0

for item in sc:
    if item == 4:
        sc.remove(item)
        taxi += 1
    elif item == 3:
        sc.remove(item)
        taxi += 1
        if 1 in sc:
            sc.remove(1)
    elif item == 2:
        sc.remove(item)
        taxi += 1
        if 1 in sc:
            sc.remove(1)
            if 1 in sc:
                sc.remove(1)
        elif 2 in sc:
            sc.remove(2)
    elif item == 1:
        sc.remove(item)
        taxi += 1
        if 1 in sc:
            sc.remove(1)
            if 1 in sc:
                sc.remove(1)
                if 1 in sc:
                    sc.remove(1)
            if 2 in sc:
                sc.remove(2)
        elif 2 in sc:
            sc.remove(2)
            if 1 in sc:
                sc.remove(1)
        elif 3 in sc:
            sc.remove(3)
print(taxi)

