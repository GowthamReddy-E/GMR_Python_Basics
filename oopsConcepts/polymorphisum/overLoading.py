class ClassA():
    def method_One(self,name=None,age=None,degree=None):
        if name==None:
            print("give any of the values at least")
        elif age==None:
            print("give age value")
        elif degree==None:
            print("give degree value")

obj=ClassA()

obj.method_One()