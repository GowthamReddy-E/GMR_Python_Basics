class  b:
    def method_1(self):
        print("this is method one in the class b")
    
    @staticmethod
    def  staticMethod():
        print("this is static method in the class b")


print(b.staticMethod())

# by using this static method annotation 
# the method will call without object also bu using class name directly