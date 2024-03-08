n = [1,2,3,4,5,7,8,9,10,12,14,15]
l= []
for ch in range(n[0],n[-1]):
    if ch not in n:
        l.append(ch)
print(l)  
