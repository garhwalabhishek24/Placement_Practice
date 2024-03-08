a="Z am Not abhay garhwalZ"
i=1
output=''
for ch in a:
    if ch.lower()=='z':
        output+=chr(ord(ch)-25)
        continue
    if ch==" ":
        output+=" "    
    else:
        output+= chr(ord(ch)+i)
print(output)


91
97
122