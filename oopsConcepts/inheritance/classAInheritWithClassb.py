class BaseClass():
    def methodOne(self):
        print("This is the method one in the base class")
    
    def methodTwo(self):
        print("this is the method two in baseclass")

    def methodThree(self):
        print("this is the method three in baseclass")


class TearDown(BaseClass):
    def methodFour(self):
        print("this is the method four in teardown class")
    
    def methodFive(self):
        print("this is the method five in teardown class")
    
    def methodSix(self):
        print("this is the method six in teardown class")
    

objectSub=TearDown()

print(objectSub.methodOne() ) 
print(objectSub.methodTwo() )
print(objectSub.methodThree())
print(objectSub.methodFour())
print(objectSub.methodFive())   
print(objectSub.methodSix())

# by creating the object of subclass we access all the methods in the super class also
# if you want to get the super class objects only you can create object of super class 
 