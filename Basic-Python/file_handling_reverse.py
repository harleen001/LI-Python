initial_file=input("Enter a file name = ")
f=open(initial_file,"w")
filecontent="abcdefghijklmnopqrstuvwxyz"
f.write(filecontent)
f.close()

f1=open(initial_file,"r")
initial=f1.read()
print("Initial file content was :",initial)
final=initial[::-1]
f1.close()

final_file = input("Enter Reversed File Name = ")
reversed_file = open(final_file, "w")
reversed_file.write((final))
print("Reversed file content is :",final)
reversed_file.close()3