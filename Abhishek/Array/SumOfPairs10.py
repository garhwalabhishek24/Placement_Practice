num = [4, 6, 5, -10, 8, 5, 20]
sum1=10
n=len(num)
for i in range(0, n):
    for j in range(i + 1, n):
        if (num[i]+num[j]==sum1):
            print("(", num[i],
                      ", ", num[j],
                      ")")
        