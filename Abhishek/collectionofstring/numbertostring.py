#input = a4k3b2
#output = aeknbd

s="a4k3b2"
output =""
for ch in s:
    if ch.isalpha():
        output = output + ch
        x = ch
    else:
        d= int(ch)
        newch = chr(ord(x)+d)
        output = output + newch
print(output)        
    
    
            
                
        