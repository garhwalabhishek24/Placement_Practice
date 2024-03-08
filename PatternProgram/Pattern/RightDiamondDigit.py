n=int(input("enter some number:"))
for i in range(n):
    for j in range(i+1):
        print(str(j+1),end=" ")
    print()    
for i in range(n-1):
    for j in range(n-i-1):   
        print(str(j+1),end=" ")
    print()    
      
      
#enter some number:4
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 
#1 2 
#1         
    