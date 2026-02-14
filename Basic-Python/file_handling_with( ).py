filename=input("Enter First Name:")
filecontent=input("Enter Your Line Contents:")
with open(filename,"w") as f:
    f.writelines(filecontent)
with open(filename,"r") as f:
    print(f.readlines())