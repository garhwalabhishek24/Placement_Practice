#To Print N number of Fabbonnic Series:
n=int(input("enter number"))
a,b,c=-1,1,0
for i in range(n):
    c=a+b 
    a=b
    b=c
    print(c,end=' ')
    
    