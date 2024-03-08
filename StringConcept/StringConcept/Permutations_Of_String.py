#enter some number:5
#1 1 1 1 1 
# 2 2 2 2 
#  3 3 3 
#   4 4 
#    5    
n=6
for i in range(n):
    print(" "*(i),end='')
    for j in range(n-i):
        print(n-j,end=" ")
    print()    