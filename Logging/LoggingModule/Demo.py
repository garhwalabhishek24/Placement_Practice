a="aaaabbbdddsss"
output=''
count=1
for i in a:
    if i in output:
        count=count+1
    print("{} occur {} time ".format(i,count))             