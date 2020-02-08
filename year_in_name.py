i = int(input())
c = i
str = ''
num = []
num.append(i%10)
while(c>=10):
    c = c/10
    c = int(c)
    num.append(c%10)

num.reverse()
while(len(num) > 0):
    # print("__= ",num[0])
    if num[0] == 0:
        str = str + ''
    elif num[0] == 1 and len(num) != 2:
        str = str + ' one'
    elif num[0] == 2:
        str = str + ' two'
    elif num[0] == 3:
        str = str + ' three'
    elif num[0] == 4:
        str = str + ' four'
    elif num[0] == 5:
        str = str + ' five'
    elif num[0] == 6:
        str = str + ' six'
    elif num[0] == 7:
        str = str + ' seven'
    elif num[0] == 8:
        str = str + ' eight'
    elif num[0] == 9:
        str = str + ' nine'

    if len(num)== 4:
        str = str + ' thousand'
        num.remove(num[0])
    elif len(num) == 3 and num[0] == 0:
        str = str + ""
        num.remove(num[0])
    elif len(num) == 3:
        str = str + ' hundread'
        num.remove(num[0])
    elif len(num) == 2 and num[0] == 0:
        num.remove(num[0])
    elif len(num) == 2 and num[0] == 1:
        if num[1] == 0:
            str = str + ' ten'
            num.remove(num[0])
        elif num[1] == 1:
            str = str + ' eleven'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 2:
            str = str + ' twelve'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 3:
            str = str + ' thirteen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 4:
            str = str + ' fourteen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 5:
            str = str + ' fifteen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 6:
            str = str + ' sixteen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 7:
            str = str + ' seventeen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 8:
            str = str + ' eighteen'
            num.remove(num[0])
            num.remove(num[0])
        elif num[1] == 9:
            str = str + ' nineteen'
            num.remove(num[0])
            num.remove(num[0])

    elif len(num) == 2:
        str = str + 'ty'
        num.remove(num[0])
    elif len(num) == 1:
        num.remove(num[0])

print(str)

# l = 2019
# lis = []
# lis.append(split(l))
# print(lis)
