initial_file=input("Enter Initial File Name:")                 #TO CREATE AN INITIAL TEXT FILE
f=open(initial_file,"a")                                       #OPEN FUNCTION TO OPEN A FILE
initial_file_content=input("Enter Your Line Contents:")        #TO GENERATE INPUT FOR THE FILE
f.writelines(initial_file_content)                             #TO WRITE LINES IN INPUT INCLUDING WHITESPACES
f.close()                                                      #CLOSE FUNCTION TO CLOSE STREAM OF FILE

with open(initial_file,"r") as initial:                        #TO OPEN THE INITIAL FILE AND READ CONTENTS
    file=initial.read()                                        #ATTRIBUTE TO READ INITIAL FILE CONTENTS
    print("Initial file content was :",file)                   #TO PRINT THE INITIAL FILE
    final = file[::-1]                                         #TO REVERSE CONTENTS OF INITIAL FILE

final_file = input("Enter Reversed File Name:")                #TO CREATE A NEW REVERSED TEXT FILE
reversed_file = open(final_file, "w")                          #TO OPEN NEWLY CREATED TEXT FILE
reversed_file.write((final))                                   #TO WRITE CONTENTS IN  NEWLY CREATED FILE
print("Reversed file content is :",final)                      #TO PRINT THE REVERSED FILE
reversed_file.close()                                          #TO CLOSE THE NEWLY CREATED FILE