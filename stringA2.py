# write a program in p to get a single string from two given strings sepreated by a space and swap the 1st two ch of each string

s1 = input("Enter string 1")
s2 = input("Enter string 2")
a = s1[0:2]
b = s2[0:2]
s1 = b + s1[2:]
s2 = a + s2[2:]
print(s1 + s2)
