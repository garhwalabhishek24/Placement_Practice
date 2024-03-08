a="Dormitory" 
b="Dirty Room"
l=[]
m=[]
for i in range(len(a)):
    flag=False  
    for j in range(len(b)):
        if b[j] ==" ":
            continue 
        for j in range(len(b)):
            if  a[i].lower()==b[j].lower():
                flag=True
                break
    if flag == False:
        break 
                
                
if flag == True:
    print("THE STRING ARA ANAGRAM")   
else:
    print("THE STRING not ANAGRAM") 
                 
                
        
    
       