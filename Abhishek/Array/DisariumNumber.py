a=135
f=str(a)
r=0 
i=0
output=0
while a!=0:
    s=a%10
    i=s
    a=a//10
for j in range(len(f),1):
    output+= i**j   
print(output)        