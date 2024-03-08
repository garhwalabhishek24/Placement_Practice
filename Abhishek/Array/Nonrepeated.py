s = "strrreeoesttttsssss"
x=''
for i in range(len(s)):
    if x==s[i]:
        continue
    
    flag= False
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            flag=True
            break
    x = s[i]
    if flag == False:
        print(s[i])
        break
    
     

        
            
            
      
        
    