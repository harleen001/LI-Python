gen = input("enter the sex of the employee (M or F) : ")
sal = int(input("enter the salary"))
if (gen == 'm' or 'M'):
    bonus=0.05*sal
    print("you'll get extra 5% bonus on your salary ")
if (gen == 'f' or 'F'):
    bonus=0.10*sal
    print("you'll get extra 10% bonus on your salary")
else:
    print("invalid input")
print("your salary = %d " % sal)
print("your bonus = %d " % bonus)
amt=sal+bonus
print("salary = %d" % amt)