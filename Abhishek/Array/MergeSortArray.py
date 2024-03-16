a = [-7, 12, 17, 29, 41, 56, 79] 
b = [-9, -3, 0, 5, 19]
n=len(a)+len(b)
l=[0]*n
k=0
for i in range(n):
    if (i<len(a)):
        l[i]=a[i]
    else:
        l[i]=b[k]
        k=k+1
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)                      