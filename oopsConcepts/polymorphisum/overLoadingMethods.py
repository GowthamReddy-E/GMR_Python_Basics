class MyClass:
    def my_method(self, arg1, arg2=None):
        if arg2 is None:
            print(f"arg1: {arg1}")
        else:
            print(f"arg1: {arg1}, arg2: {arg2}")

obj = MyClass()

obj.my_method(10)  # Output: arg1: 10

obj.my_method(10, 20)  # Output: arg1: 10, arg2: 20