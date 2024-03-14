n=1252
i=0
r=0
output1=0
Falg=True
while n!=0:
    output=n%10
    i = output
    n=n//10
    output1+=i
print(output1)    
a=output1
r=0
while output1!=0:
    a=a%10
    r=a
    if r == 0 or 1:
        Falg==False
if Falg==False:
    print("this is magic number")
if Falg==True:
    print("this is not magic number")            
    
    
    
    
    

   
   
    