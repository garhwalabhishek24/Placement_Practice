a=[1,2,3,4,5,6,7,8,9]
sum1=10
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==sum1:
            print((a[i],a[j]))