a=137
n=a
f=str(a)
r=0 
i=0
output=0
num=int(len(f))   
while a!=0:
    s=a%10
    i=s
    a=a//10
    output+=i**num 
    num=num-1 
if n==output:
    print("it is a Disarium Number")
else:
    print("it not a Disarium Number")          