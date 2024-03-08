n = int(input("enter number"))
a=n
i=0

while n!=0:
    output=n%10
    i+=output *output*output
    n=n//10    
if i == a:
    print("it is a Armstron")
else:
    print("it is not  a Armstron")
    
   
    
    




#
# for i in str(153):
#     num1=int(i)
#     output += (num1*num1*num1)    
# if output == n:
#     print("it is a Armstron")
# else:
#     print("it is not  a Armstron")
#

    