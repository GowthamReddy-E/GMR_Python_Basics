name ="gowtham"

class details:
    name="reddy"
    
    @staticmethod
    def details_gowtham(name):
        print(name)
        print(details.name)
        print(globals()['name'])

print(details().details_gowtham("eragamreddy"))
