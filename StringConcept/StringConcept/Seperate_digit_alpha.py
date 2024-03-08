a="I3 A2M N7O4T A1B8H3AY G1AR9H0W4A6L1"
alpha=""
digits=""
for ch in a:
    if (65<=ord(ch)<=90) or (97<=ord(ch)<=122):
        alpha+=ch
    else:
        digits+=ch
print(alpha)
print(digits)            