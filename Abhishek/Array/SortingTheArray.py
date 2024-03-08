a=[5,34,78,2,45,1,99]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp        
print(a)        
        