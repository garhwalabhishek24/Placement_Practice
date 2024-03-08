n=int(input("enter some number:"))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
    
# enter some number:4
#    A 
 #  A B 
#  A B C 
# A B C D 
            