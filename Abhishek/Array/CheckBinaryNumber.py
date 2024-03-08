s=11001110000-1
r=0
while s!=0:
    flag=False
    d=s%10 
    r=r*10+d
    s=s//10
    if r==1 or 0:
        flag=False
    else:
        flag=True
if flag==False:
    print("the number is binary ")
else:
    print("the number is not binary")               
        
    
    
