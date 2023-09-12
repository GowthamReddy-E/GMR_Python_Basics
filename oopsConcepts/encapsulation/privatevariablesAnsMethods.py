class classA():

    __name="gowtham reddy"

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name
        print(self.__name)

    def __methodOne(self):
        print("this is private method one in the class a"+self.getName())
    

    def getMethodOne(self):
        return self.__methodOne()
    

obj=classA()

obj.setName("eragamreddy")
print(obj.getName())
print(obj.getMethodOne())
