s = "To change this license header, choose License Headers in Project Properties"
# char c1 = 'o';
# char c2 = 'h';'''
s1=s.split()
o='o'
h='h'
l=[]
se = ""
for word in s1:
    for i in word:
        if i == 'o' or i == 'h':
            l.append('@')
        else:
            l.append(i) 
            
            
    for j in l:
        if j != '@':
            se += j               
print(se)            
                  
         
    
            
            
