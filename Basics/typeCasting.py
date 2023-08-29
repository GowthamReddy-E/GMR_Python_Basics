numberOne=input("give first number :")
numberTwo=input("give second number :")


# method one use only int typecast

print("before typecasting")
print(numberOne+numberTwo)
print("after typecasting")
print(int(numberOne)+int(numberTwo))

# method two use only float typecast

print("before typecasting")
print(numberOne+numberTwo)
print("after typecasting")
print(float(numberOne)+float(numberTwo))


# the int typecast dosnt typecast the float values
# float typecast will work both int and float values