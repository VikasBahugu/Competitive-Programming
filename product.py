inp = int(input())
num = list(map(int, input().split()))
res = 1
fat = pow(10,9) + 7
print(fat)
for item in num:
    res = (res * item) % fat
print(res)