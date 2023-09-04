class class_A():
    def addTwoValues(self,a,b):
        print(a+b)


    @staticmethod
    def add(self):
        print(self)



print(class_A().addTwoValues(12,20))
print(class_A().add(20))

