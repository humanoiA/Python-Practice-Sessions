from abc import *
class peter(ABC):
    @abstractmethod
    def inpt(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Rect(peter):
    def inpt(self):
        self.b=int(input("enter length: "))
        self.a=int(input("enter breadth: "))
    def area(self):
        area=self.a*self.b
        print('Area of rect is : ',area)

class Sqr(peter):
    def inpt(self):
        self.b=int(input("enter length: "))
    def area(self):
        area=self.b*self.b
        print('Area of sqr is : ',area)
class Circle(peter):
    def inpt(self):
        self.b=int(input("enter radius: "))
    def area(self):
        area=self.b*self.b*3.14
        print('Area of circle is : ',area)

ob=Rect()
ob.inpt()
ob.area()
del ob
ob=Sqr()
ob.inpt()
ob.area()
del ob
ob=Circle()
ob.inpt()
ob.area()