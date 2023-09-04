def keyValueFUnction(name,age,gender):
    print(name,age,gender)


keyValueFUnction("gowtham",27,"Male")


keyValueFUnction(gender="Male",age=27,name="Gowtham")

# if you brake the keyvalue arguments it dosnt work 
# the condition is like 

# first value and then keyvalue pair only
keyValueFUnction(gender="Male",age=27,name="Gowtham")   # it works
# keyValueFUnction(gender="Male",age=27,"Gowtham")  # it dosnt works
keyValueFUnction("Male",age=27,name="Gowtham")       # it dosnt works
