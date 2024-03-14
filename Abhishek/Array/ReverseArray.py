a=[1,2,3,4,5,6,7,8,9,10]
num=len(a)-1
start=0
while (start<num):
    temp=a[start]
    a[start]=a[num]
    a[num]=temp
    start=start+1
    num=num-1
print(a)


    