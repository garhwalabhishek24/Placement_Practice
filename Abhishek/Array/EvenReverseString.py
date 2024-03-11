s="one,two,three,four,five,six,seven,eight,nine,ten"
s1=s.split()
i=0
l=[]
while i<len(s1):
    if i%2==0:
        l.append(s1[i][::-1])
    i=i+1
print(l)    
        
                     
      