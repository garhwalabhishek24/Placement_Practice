a=[7, -5, 3, 8, -4, 11, -19, 21]  
b=[6, 13, -7, 0, 11, -4, 3, -5]
n=a+b
s=[]
m=len(s)
l=[0]*m

for i in n:
    if i not in s:
        s.append(i)
for i in range(m):
    l[i]=s[i]
            
print(l)            
# for i in range(m):
#     for j in range(i+1,m):
#         if (l[i]>l[j]):
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp






