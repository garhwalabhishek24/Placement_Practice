k = "hello a world java javatpoint" 
#   tniop t avaja vajd lrowaolleh
s=k.split()
output=''
output1=''
i=len(s)-1
lwithoutSpace=[]
lWithSpace=[]
while i>=0:
    output += s[i][::-1]
    i=i-1
for i in k:
    lwithoutSpace.append(i)   
for i in output:
    lWithSpace.append(i)
    
g = 0
for i in range(len(lwithoutSpace)):
    
    if lwithoutSpace[i] == ' ':
        continue;
    else :
        lwithoutSpace[i] = lWithSpace[g]
        g = g+ 1
        
        
for i in lwithoutSpace:
    output1+=i
print(output1)    


   
    



    
