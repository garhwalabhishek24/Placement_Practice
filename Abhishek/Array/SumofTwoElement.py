arr= [5, 34, 78, 2, 45, 1, 99, 23]
sum1=0
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)): 
        sum1=arr[i]+arr[j]
    print(sum1)     
   