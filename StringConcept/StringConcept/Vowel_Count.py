s="i am not abhay garhwal"
vowel="aeiou"
output=''
for i in range(len(s)):
    for j in range(len(vowel)):
        if s[i]== vowel[j]:
            output+=vowel[j]
print(output)            