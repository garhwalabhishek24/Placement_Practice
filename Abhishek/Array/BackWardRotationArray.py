a=[3,4,2,1, 5, 6, 7,8]
n=3
b=len(a)-1
output=''

while n<len(a):
    output+=str(a[n])
    n=n+1    
for j in range(len(output)):
    a[b]=int(output[j])
    b=b-1
    
print(a)        
       
           
            
         
 
                
    
    
    