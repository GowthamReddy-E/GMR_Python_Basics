class ClassA():
    def method_one(self):
        print("this is the method one in the class a")
    
    
    def method_two(self):
        print("this is the method two in the class a")
    
    
    def method_three(self):
        print("this is the method three in the class a")
    
class ClassB(ClassA):
    def method_four(self):
        self.method_one()
        print("this is the method four in class b")
    
    def method_five(self):
        super().method_two()
        print("this is the method five in class b")
    
    def method_six(self):
        ClassA().method_three()
        print("this is the method six in class b")
        
    

    
obj=ClassB()

print(obj.method_four())

print(obj.method_five())

print(obj.method_six())
