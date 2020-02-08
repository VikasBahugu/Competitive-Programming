L = int(input())
N = int(input())
#Creating an empty template.
lst = [[0] * 2 for i in range(N)]

for i in range(0,N):
    lst[i] = list(map(int, input().split()))

for x in range(0,len(lst)):
    for y in range(0,1):
        if lst[x][y] > L and lst[x][y+1] > L:
            if lst[x][y] == lst[x][y+1]:
                print("ACCEPTED")
            else:
                print("CROP IT")
        elif lst[x][y] < L or lst[x][y+1] < L:
            print("UPLOAD ANOTHER")