a=[5, -9, 4, -2, 7, 1, -4, -3, -7]
sum=-7
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j]==sum):
            print((a[i],a[j]))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for z in range(j+1,len(a)):
            if (a[i]+a[j]+a[z])==sum:
                print((a[i]+a[j]+a[z]))
                           
            
           
           
             
            