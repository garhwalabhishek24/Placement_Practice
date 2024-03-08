n=8
a,b,c=-1,1,0 
for i in range(n+1):
    c=a+b 
    #print(c)
    a=b
    b=c
    if n==c:
        print("the number is in series")
        break;
    elif c > n:
        print("the number not is in series")
        break;   

    
        
    
    
    
         

   
