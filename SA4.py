s1 = input("enter string")
if len(s1) >= 3:
    if s1.endswith('ing'):
        s1 = s1+'ly'
    else:
        s1 = s1 + "ing"
print(s1)
