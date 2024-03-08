a=[0,1, 2, 9, 4, 5, 6, 7,8]
num=len(a)-1
output=""
for i in range(len(a)):
    output+=str(a[num])
    num=num-1
for j in range(len(output)):
    a[j] = int(output[j])       
 
print(a)           