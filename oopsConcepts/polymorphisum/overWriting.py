class classA():
    def methodOne(self):
        print("this is the method one in the classA")
        print(20+30)
    
    
class classB(classA):

    def methodOne(self):
        print("this is method one in the classB")
        print(30+40)
    
obj=classA()
print(obj.methodOne())

obj=classB()
print(obj.methodOne())