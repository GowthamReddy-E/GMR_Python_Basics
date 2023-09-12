class classA():

    __name=None
    __village=None
    __Age=None
    __hight=None

    def setName(self,name):
        self.__name=name
    
    
    def setVillage(self,village):
        self.__village=village
    
    
    def setAge(self,age):
        self.__Age=age
    
    
    def setHight(self,hight):
        self.__hight=hight


    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__Age
    
    def getVillage(self):
        return self.__village
    
    def getHight(self):
        return self.__hight
    

obj=classA()

print(obj.setName("gowtham"))
print(obj.setVillage("Thummalapalli"))
print(obj.setAge(27))
print(obj.setHight(5))

print(obj.getName())
print(obj.getVillage())
print(obj.getAge())
print(obj.getHight())