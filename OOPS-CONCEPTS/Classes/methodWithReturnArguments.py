class c:
    def method_1(self,a,b):
        return a+b
    
    
    def method_2(self,a,b):
        return a*b,a+b


obj= c()

print(obj.method_1(10,20))

print(obj.method_2(10,20))

print(type(obj.method_2(10,20)))
# if the method is return multiple values the output type is tuple