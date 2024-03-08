s=input("enter some string")
s1= s.split() 
l = []
i=0
while i<len(s1):
    
    if i%2==0:
        l.append(s1[i])
    else:
        l.append(s1[i][::-1])
    i = i+1 
output = " ".join(l)
print(output)           
        
    
     