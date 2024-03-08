s = "java2novice"     #output:- a2novice
a=''
output=''
for i in range(1,len(s)):
    if a==s[i]:
        continue
    
    flag= False
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            flag=True
            break
    a= s[i]
    if flag == False:
        output+=s[i]
        print(s[i])
        
        