a="I Am Not Abhay Garhwal"
i=1
output=''
for ch in a:
    if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122) :
        output+= chr(ord(ch)+i) 
    if ch==" ":
        output+=" "       
print(output)        
     
          
    
     