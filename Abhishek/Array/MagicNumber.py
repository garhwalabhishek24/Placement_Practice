n=-2010
i=0
r=0
output1=0
if n<10:
    print("it is not a magic number")
while n!=0:
    output=n%10
    i = output
    n=n//10
    output1+=i  
print(output1)      
if output1==10:
    print("it is a magic number")
else:
    print("it is not a magic number")    
    
    
    
    
    

   
   
    