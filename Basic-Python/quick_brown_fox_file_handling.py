string_file=input("Enter Initial File Name:")
s=open(string_file,"w")
string_file_content=input("Enter Your Line Contents:")
s.writelines(string_file_content)
s.close()
list1=[]
list2=[]
list3=[]
with open(string_file,"r") as string:
    str_1=string.read()
    print("String file content was :",str_1)
    for i in str_1:
        if i in "aeiou":
            list1.append(i)
    for j in str_1:
        if j in "bcdfghjklmnpqrstvwxyz":
            list2.append(j)
    for k in str_1:
        if k in " ":
            list3.append(k)
vowel_file= input("Enter Vowel File Name:")
vowels_file = open(vowel_file, "w")
vowels_file.write(str("Vowels are")+(str(list1)))
print("Vowels are:",list1)
vowels_file.close()

consonant_file= input("Enter Consonants File Name:")
consonants_files = open(consonant_file, "w")
consonants_files.write(str("Consonants are")+(str(list2)))
print("Consonants are:",list2)
vowels_file.close()
a=len(list1)
b=len(list2)
c=len(list3)
summarie_file= input("Enter Summary File Name:")
summary_files = open(summarie_file, "w")
summary_files.write(str("Vowels are:")+(str(a)))
print("Vowels are:",a)
summary_files.write(str("\nConsonants are:")+(str(b)))
print("Consonants are:",b)
summary_files.write(str("\nWhitespaces are:")+(str(c)))
print("Whitespaces are:",c)
summary_files.close()
