n=input('enter no:')
n=int(n)
while n>0:
    x = n%10

    sum = sum + x
    n = n//10
    print(sum)

 n=input("enter no:")
 n=int(n)
 sum=1
 while n>0:
     x=n%10
     sum=n//10
     print(sum)