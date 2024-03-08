# a occur 3  times 
# b occur 4  times 
# s occur 2  times 
# d occur 3  times 
# e occur 1  times 
# w occur 1  times 

s="aaabbbbssdddew"
d={}
for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in d.items():
    print('{} occur {}  times '.format(k,v))                        

