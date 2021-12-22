class test:
    """
    this is test class
    this show how instant variable works
    """
    def __init__(self,x,y):
        """
        param x: this is value of i
        param y: this is valude of j
       self.i=x
       self.j=y
        """
    def add(self):
        """
        return gives condition of 2 int

        """
        print(self.i + self.j)
        print(test.__name__)
        print(test.__module__)
        print(test.__bases__)
t1=test(10,20)
print(t1.__dict__)
t2=test(30,40)
print(t2.__dict__)
print(dir(t1))
print(test.__doc__)
print(t1.__init__.__doc__)
print(t1.add.__doc__)


