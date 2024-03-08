s="I3 A2M N7O4T A1B8H3AY G1AR9H0W4A6Z2"
output=''
i=1
for ch in s:
    if ch.isalpha():
        if ch.lower()=='z':
            output+=chr(ord(ch)-25)
            continue
        else:
            output+= chr(ord(ch)+i)
    
    elif ch==" ":
        output+=" "          
    else:
        if ch.isalnum():
            output+= str(int(ch)+i)
print(output)