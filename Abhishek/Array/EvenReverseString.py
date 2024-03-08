s="one,two,three,four,five,six,seven,eight,nine,ten"
s1=s.split()
i=0
l=[]
for ch in s1:
    if i%2==0:
        l.append(ch[i][::-1])
      