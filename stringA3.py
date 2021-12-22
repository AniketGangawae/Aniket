# write a program to get a string from a given string when all occurches  of its 1st ch have been changed to $
# except the 1st char itslef
# sample restart = resta$t


s1 = input(" enter string")
print(s1)
s1 = s1[0]+s1[1:].replace (s1[0], "$")
print(s1)
