# write a p.p ti count the no of ch. in a string

s1 = "google.com"
list1 = []
for x in s1:
 i = 0
 if x not in list1:
    for y in s1:
        if x == y:
            i = i + 1
    print(x, "occurs", i, "times")
    list1.append(x)
