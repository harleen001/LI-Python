spaces_file=input("Enter Initial File Name:")
s=open(spaces_file,"w")
spaces_file_content=input("Enter Your Line Contents:")
s.writelines(spaces_file_content)
s.close()
list1=[]
with open(spaces_file,"r") as space:
    spc=space.read()
    print("Space file content was :",spc)
    for i in spc:
        if i not in " ":
            list1.append(i)
    def string(list1):
        str1=""
        for j in list1:
            str1=str1+j
        return str1
        print(string(list1))
filename=input("Enter Unspaced file Name:")
with open(filename,"w") as f:
    f.writelines(str("Unspaced file content is :")+str(string(list1)))
with open(filename,"r") as f:
    print(f.readlines())