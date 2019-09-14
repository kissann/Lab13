'''class MyFirstClass:
    a=15
    def ClassFunc(self):
        print(self.a)
fobj=MyFirstClass()
print(fobj.a)
fobj.ClassFunc()'''
class MyFirstClass:
    def __init__(self,a,b,c):
        self.__height=a
        self.width = b
        self.depth = c
table = MyFirstClass(0.75,1.2,0.7)
print(table.__height)
print(table.width)
print(table.depth)
