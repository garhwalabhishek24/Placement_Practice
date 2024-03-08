# 1
# 2 3
# 4 5 6
# 7 8 9 10
n= 4
num=1
for i in range(n):
    for j in range(i+1):
        print(str(num)+" ",end='')
        num+=1
    print()   