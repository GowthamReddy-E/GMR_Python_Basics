name="gowtham"    # global variable

def details(age,name):   # local variable
    
    global degree                # global variable set at function level
    degree="M-tech"
    print(age)
    print(name)
    print(globals()['name'])
    print(degree)

def global_Variable_print():
    print(name)
    print(degree)

details(27,"reddy")
global_Variable_print()