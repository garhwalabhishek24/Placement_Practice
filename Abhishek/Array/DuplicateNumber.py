arr=[1,2,3,2,3,4,3,6,5,4,6,4,8,8,5,6,3]
for i in range(len(arr)):
    count=1
    if arr[i]==0:
            continue
    for j in range(i+1,len(arr)):
        
        if arr[i]==arr[j] :
            count=count+1
            arr[j] =0
    print("{} occur {} times ".format(arr[i],count))            
            
               
    

