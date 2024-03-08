a=[45, 84, 101, 62, 12, 45]
for i in range(len(a)):
    for j in range(i+1):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)            