from numpy import single


class Person:#defining the class we are using
    def __init__(self,age,height):#the init method takes three objects
        self.age=age#assigning variables to the class
        self.height=height
    def printname(self):#defining the method
        print(self.age,self.height)
class student(Person):#defining the class we are using
    def single(self,age,height):
       super().__init__(age,height)#calling the super class
    def welcome(self):
        print(self.age,"is your age\n",self.height,"is your height")#printing from the class

x=student(23,12)
x.welcome()