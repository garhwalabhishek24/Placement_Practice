a=[5,4,2,3,9,1,2,4]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[j])
            break
       