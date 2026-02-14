def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

a = int(input("Enter value before swap: "))
b = int(input("Enter value before swap: "))
print("Before swap value of a=", a)
print("Before swap value of b=", b)

a,b = swap(a,b)
print("After swap value of a=", a)
print("After swap value of b=", b)
