from abc import *
# import abc
class classA(ABC):
    @abstractmethod
    def methodOne(self):
        print("this is abstract method")

class classB(classA):

    def methodTwo(self):
        print("this is the methodTwo in the classB")
    
    def methodOne(self):
        print("converted into concrete method")

obj=classB()
obj.methodTwo()
obj.methodOne()

# compulsory converted into abstract method into concrete method
# if not it will throw the error
# you can converted abstract methods in multi classes also