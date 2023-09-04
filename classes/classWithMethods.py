class class_A():
    def addTwoValues(a,b):
        print(a+b)

    
    @staticmethod
    def add(self):
        print(self)



print(class_A.addTwoValues(12,20))
print(class_A().add(12))