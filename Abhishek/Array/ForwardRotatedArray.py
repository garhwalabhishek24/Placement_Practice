a=[3,4,2,1, 5, 6, 7,8]
n=3
output1=''
 
for i in range(n):
    output1+= str(a[i])
k =len(output1)-1     
for j in range(len(output1)):
    a[j]=int(output1[k])
    k=k-1
print(a)
 

       
    