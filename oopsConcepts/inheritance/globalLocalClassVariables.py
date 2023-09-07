name="Gowtham global"
age="27 global"

class ClassAA():
    name="Gowtham class"
    age="27 class"
    def methodOne(self,name,age):
        print(name,age)

class ClassBB(ClassAA):
    name="Gowtham subClass"
    age="27 subclass"
    def methodTwo(self,name,age):
        self.methodOne("gowtham super class name","27 super class age")
        print("local Variables : ",name,age)
        print("class Variables : ",self.name,self.age)
        print("super class Variables : ",super().name,super().age)
        print("global Variables : ",globals()['name'],globals()['age'])
    

obj=ClassBB();

print(obj.methodTwo("gowtham",27))