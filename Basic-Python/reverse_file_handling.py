filename=input("Enter File Name:")
f=open(filename,"a")
f.write(("abc"))
f.close()

with open(filename,"r") as file:
    file1=file.read()
    print(file1)

with open(filename,"w") as file:
    file2=file1[::-1]
    file.write(file2)
    print(file2)