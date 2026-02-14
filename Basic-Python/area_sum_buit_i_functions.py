
def area(length,breadth):
    area = int(length)*int(breadth)
    return area
def perimeter(length,breadth):
    perimeter =(int(length)+int(breadth))*2
    return perimeter

num1=input("Enter Ist Number = ")
num2=input("Enter 2nd Number = ")
print(area(num1,num2))
print(perimeter(num1,num2))