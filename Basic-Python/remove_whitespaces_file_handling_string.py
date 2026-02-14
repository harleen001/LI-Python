spaces_file=input("Enter Initial File Name:")
s=open(spaces_file,"w")
spaces_file_content=input("Enter Your Line Contents:")
s.writelines(spaces_file_content)
s.close()
str1=""
with open(spaces_file,"r") as space:
    spc=space.read()
    print("Space file content was :",spc)
    for i in spc:
        if i not in " ":
            str1+=i
    print(str1)

filename=input("Enter Unspaced file Name:")
with open(filename,"w") as f:
    f.writelines("Unspaced file content is :"+str1)
with open(filename,"r") as f:
    print(f.readlines())