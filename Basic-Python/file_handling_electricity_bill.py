filename=input("Enter your bill filename : ")
f=open(filename,"w")
for i in range(1,51):
    print("Fill records of Consumer number", i)
    name=input("Enter Name of Consumer : ")
    f.writelines(name)
    accno=input("Enter Account number of Consumer : ")
    f.writelines(accno)
    unit=input("Enter Unit consumed of Consumer : ")
    f.writelines(unit)
    amt=input("Enter Bill amount of Consumer : ")
    f.writelines(amt)
    i=i+1
f.close()