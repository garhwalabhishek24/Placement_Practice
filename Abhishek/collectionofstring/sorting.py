#input =b4a1d3
#output = abc143

s="B4A1D3"
alpbhabet=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alpbhabet.append(ch)
    else:
        digit.append(ch)
output="".join(sorted(alpbhabet) + sorted(digit))
print(output)            