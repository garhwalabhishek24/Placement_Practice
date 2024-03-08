k = "hello a world java"
s1=k.split()
l=[]
i=0
while i>=0:
    if i%2==0:
        l.append(i[::-1])
    else:
        l.append(i)  
print(l)         

