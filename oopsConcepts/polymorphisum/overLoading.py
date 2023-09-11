class ClassA():
    def method_One(self,name=None,age=None,degree=None):
        if name==None:
            print("write logics if name equal to none")
        elif age==None:
            print("write logics if name equal to none")
        elif degree==None:
            print("write logics if name equal to none")
        else:
            print("write default logics")

obj=ClassA()

obj.method_One()