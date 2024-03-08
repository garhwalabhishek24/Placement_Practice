s="a3b3d4c3"
d={}
output=""
x=0
for ch in s:
    if ch.isalpha():
        x= ch
    else:
        d= int(ch)
        output = output+ x*d
print(output)           
        