a='a4b3d2'
b='xyz'
c='1234567890'
output=''
i=j=k=0
while i<len(a) or j<len(b)or j<len(c):
    if i<len(a):
        output=output+a[i]
    i=i+1
    if  j<len(b):
        output=output+b[j]
    j=j+1
    if k<len(c):
        output=output+c[k]
    k=k+1
print(output)        
            
        