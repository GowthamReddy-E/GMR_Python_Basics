class Class_A():
    def  method_1(self):
        print("this is method one in the class a" )

    def method_2(self):
        print("this is method two in the class a" )
    
    
    def method_3(self):
        print("this is method three in the class a" )


class Class_B():

    def  method_4(self):
        print("this is method 4 in the class a" )

    def method_5(self):
        print("this is method 5 in the class a" )
    
    
    def method_6(self):
        print("this is method 6 in the class a" )


objectA=Class_A()
objectB=Class_B()

print(objectA.method_1())
print(objectA.method_2())
print(objectA.method_3())


print(objectB.method_4())
print(objectB.method_5())
print(objectB.method_6())


# without inheritance you can create an object that object will call only that class methods 
# if you want to call both class a and class b you need to compulsory inherit with class b 
