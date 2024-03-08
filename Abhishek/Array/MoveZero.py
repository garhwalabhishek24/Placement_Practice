arr = [2,3,0,5,3,0,0,7,5,0,2]
sum1=''
for i in range(0, len(arr)): 
    if arr[i]!=0:
        sum1+= str(arr[i])
        arr[i]=0        
        
for j in range(len(sum1)):
    arr[j] = int(sum1[j])       
 
print(arr) 
            
                   
         
      
   
      
    
        
    