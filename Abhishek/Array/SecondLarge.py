arr = [5, 34, 78, 2, 45, 1, 99, 23]
largest= arr[0]
secondlarge=arr[0]
for num in arr:
    if num > largest:
        secondlarge =largest
        largest = num
print(secondlarge)        
         