A = [-7, 12, 17, 29, 41, 56, 79] 
B = [-9, -3, 0, 5, 19]
i=0
n=len(A)+len(B)
l=[0]*5 
k = 0
for i in range(n):
    if (i < len(A)):
        l[i]=A[i]
    else:
        
        l[i]=B[k]
        k=k+1    
print(l)     