a='JavaConceptJOfTheDay'
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[0]==a[j]:
            print(a[j]) 
        break  
count=1      
for i in  range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count=count+1
            i=i+1
        if count==1:
            print(a[j])            
            
    
    
    
            


         