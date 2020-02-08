a = list(input())
ls = []
temp = 0
for item in a:
    if item.isupper():
        ls.append(item.lower())
    else:
        ls.append(item.upper())
for i in range(0,len(ls)):
    print(ls[i],end= "")

# def uppss(str):
#     if str.isupper():
#         print(str.lower(),end="")
#     else:
#         print(str.upper(),end="")
#     xi += 1
# i=0
# x = list(input())
# le = len(x)
# xi= 0
# while(xi != le):
#     uppss(x[i])
#     i += 1