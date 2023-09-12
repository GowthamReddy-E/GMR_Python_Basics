from abc import ABC,abstractmethod
class classA(ABC):
    @abstractmethod
    def methodOne(self):
        print("abstract methodOne")
    
    @abstractmethod
    def methodTwo(self):
        print("abstract methodTwo")
    
class classB(classA):

    def methodOne(self):
        print("concrete methodOne")
    
class classC(classB):
    def methodTwo(self):
        print("concrete methodTwo")
    

obj=classC()

obj.methodOne()
obj.methodTwo()