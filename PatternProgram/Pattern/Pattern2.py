n=int(input("enter some number:"))
for i in range(n):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print(n-j,end=" ")
    print()
   
#enter some number:5
#    5 
#   5 4 
#  5 4 3 
# 5 4 3 2 
#5 4 3 2 1 
   
    