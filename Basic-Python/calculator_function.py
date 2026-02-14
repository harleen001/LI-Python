#MAKING CALCULATOR FUNCTION
def calc(num1, num2):
    return num1+num2,num1-num2,num1*num2,num1/num2
addition,substraction,multiplication,division = calc(5,2)
print("ADDITION =",addition)
print("SUBSTRACTION =",substraction)
print("MULTIPLICATION =",multiplication)
print("DIVISION =",division)