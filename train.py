no = int(input()) #Input test cases iteration
cas = []
for i in range(0, no):
    cas.append(int(input()))    #input for no test cases.
ws = []
ms = []
es = []
op = []
#Logic for Window Seat.
def wst(w):
    if w%6==0 or w%6==1 or w == 1:
        ws.append(w)
        return True
    else:
        return False

#Logic for middle seat.
def mst(w):
    a = wst(w-1)
    b = wst(w)
    c = wst(w+1)
    if (a == True and b == True) or (b == True and c == True):
        return False

    elif (a == True or c == True):
        ms.append(w)
        return True

#Logic for eyle seat
def est(w):
    l = wst(w)
    m = mst(w)
    if l != True and m != True:
        es.append(w)

#Logic for passenger opposite to given seat.
def ops(w):











    n = 1
    for i in range(1,10):
        for j in range(n,n+12):
            if w  == j:
                print(w)
                seat1 = wst(w)
                seatw = wst(w)
                seat2 = mst(w)
                seatm = mst(w)
                seat3 = est(w)
                # For passenger opp to window seat
                if seat1 == True:
                    if (i + 12) / 2 < w:
                        seatnex = wst(w + 1)
                        if seatnex == True:
                            op.append(w + 1)
                        else:
                            op.append(w + 11)
                    else:
                        seatnex = wst(w - 1)
                        if seatnex == True:
                            op.append(w - 1)
                        else:
                            op.append(w - 11)

                #For passenger opp to middle seat
                elif(seatw != True):
                    #only then, check for middle seat
                    if seat2 == True:
                        if (i + 12) / 2 < w:
                            seatnex = wst(w-1)
                            if seatnex == True:
                                op.append(w+9)
                            else:
                                op.append(w+3)
                        else:
                            seatnex = wst(w-1)
                            if seatnex == True:
                                op.append(w+9)
                            else:
                                op.append(w+3)

                    #For passenger opp to eyle seat
                    else:
                        #only then check for eyle seat
                        if seat3 == True:
                            if (i + 12) / 2< w:
                                seatnex = wst(w+2)
                                if seatnex == True:
                                    op.append(w+5)
                                else:
                                    op.append(w+7)
                            else:
                                seatnex = wst(w-2)
                                if seatnex == True:
                                    op.append(w-5)
                                else:
                                    op.append(w-7)


for w in cas:
    wst(w)
ws_unique = list(set(ws))
print(ws_unique)
for w in cas:
    mst(w)
ms_unique = list(set(ms))
print(ms_unique)
for w in cas:
    est(w)
es_unique = list(set(es))
print(es_unique)
for w in cas:
    ops(w)
op_unique = list(set(op))
print(op_unique)






#Logic for total seats from 1 to 9 cells.
# n = 1
# for i in range(1,10):
#     for j in range(n,n+12):
#         print("Cell: ",i,"  passenger: ",j)
#     n = n + 12



# #Logic for passenger opposite to given seat.
# def ops(w):
#     n = 1
#     for i in range(1,10):
#         for j in range(n,n+12):
#             if w  == j:
#                 seat1 = wst(w)
#                 seatw = wst(w)
#                 seat2 = mst(w)
#                 seatm = mst(w)
#                 seat3 = est(w)
#                 # For passenger opp to window seat
#                 if seat1 == True:
#                     if (i + 12) / 2 < w:
#                         seatnex = wst(w + 1)
#                         if seatnex == True:
#                             op.append(w + 1)
#                         else:
#                             op.append(w + 11)
#                     else:
#                         seatnex = wst(w - 1)
#                         if seatnex == True:
#                             op.append(w - 1)
#                         else:
#                             op.append(w - 11)
#
#                 #For passenger opp to middle seat
#                 elif(seatw != True):
#                     #only then, check for middle seat
#                     if seat2 == True:
#                         if (i + 12) / 2 < w:
#                             seatnex = wst(w-1)
#                             if seatnex == True:
#                                 op.append(w+9)
#                             else:
#                                 op.append(w+3)
#                         else:
#                             seatnex = wst(w-1)
#                             if seatnex == True:
#                                 op.append(w+9)
#                             else:
#                                 op.append(w+3)
#
#                     #For passenger opp to eyle seat
#                     else:
#                         #only then check for eyle seat
#                         if seat3 == True:
#                             if (i + 12) / 2< w:
#                                 seatnex = wst(w+2)
#                                 if seatnex == True:
#                                     op.append(w+5)
#                                 else:
#                                     op.append(w+7)
#                             else:
#                                 seatnex = wst(w-2)
#                                 if seatnex == True:
#                                     op.append(w-5)
#                                 else:
#                                     op.append(w-7)
