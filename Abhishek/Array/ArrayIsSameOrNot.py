arr=[4,3,2,1,5]
arr1=[4,3,2,1,0]

if len(arr)!=len(arr1):
    print("the array is not equal")
        
        
for i in range(len(arr)):
    flag=False  
    for j in range(len(arr1)):
        if  arr[i]==arr1[j]:
            flag=True
            break
    if flag == False:
        break       
            
            
if flag==True:
    print("the array are equal")
else:
    print("the array is not equal")
    
                     