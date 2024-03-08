s=input("enter some word to reverse :")
s1 = s.split()
l =[]
for word in s1:
    l.append(word[::-1])
output = " ".join(l) 
print(output)   
    