#list1=[ i for i in range (10)]
#print(list1)

#list1=[i*i for i in range(10)]
#print(list1)

def sqr(x):
    z = x * x
    return 2
list1=[sqr(i) for i in range (10)]
print(list1)
