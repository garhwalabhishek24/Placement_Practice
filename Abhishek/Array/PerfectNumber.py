n = int(input("enter some number"))
sum1=0
for i in range(1,n):
    if n%i==0:
        sum1+=i
if sum1==n:
    print("its a perfect number")
else:
    print("its not perfect number")            
        



        
     