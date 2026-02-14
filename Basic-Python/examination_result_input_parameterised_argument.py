class reportcard:                                                                           #REPORT CARD IS CLASS
                                                                                            #USING CALL BY REFERENCE AND CALL BY VALUE (PARAMETERISED)
  def examination(self,name,rollno,phymarks,chemmarks,mathsmarks,ipmarks,engmarks):         #EXAMINATION IS A FUNCTION DEFINED IN DYNAMIC CLASS FOR INPUT OF DATA
    self.name=name                                                                          #OBJECT NAME IS VALUELIZED
    self.rollno=rollno                                                                      #OBJECT ROLLNO IS VALUELIZED
    self.phymarks=phymarks                                                                  #OBJECT PHYSICS MARKS IS VALUELIZED
    self.chemmarks=chemmarks                                                                #OBJECT CHEMISTRY MARKS IS VALUELIZED
    self.mathsmarks=mathsmarks                                                              #OBJECT MATHS MARKS IS VALUELIZED
    self.ipmarks=ipmarks                                                                    #OBJECT IP MARKS IS VALUELIZED
    self.engmarks=engmarks                                                                  #OBJECT ENGLISH MARKS IS VALUELIZED

  def result(self):                                                                         #RESULT IS A FUNCTION DEFINED IN DYNAMIC CLASS FOR OUTPUT OF DATA

    print("student name =",self.name)                                                       #FOR PRINTING NAME OF THE STUDENT
    print("student rollno =",self.rollno)                                                   #FOR PRINTING ROLLNO OF THE STUDENT
    print("student physics marks =",self.phymarks)                                          #FOR PRINTING PHYSICS MARKS OF THE STUDENT
    print("student chemistry marks =",self.chemmarks)                                       #FOR PRINTING CHEMISTRY MARKS OF THE STUDENT
    print("student maths marks =",self.mathsmarks)                                          #FOR PRINTING MATHS MARKS OF THE STUDENT
    print("student IP marks =",self.ipmarks)                                                #FOR PRINTING IP MARKS OF THE STUDENT
    print("student english marks =",self.engmarks)                                          #FOR PRINTING ENGLISH MARKS OF THE STUDENT
    total=(self.phymarks+self.chemmarks+self.mathsmarks+self.ipmarks+self.engmarks)         #TO CALCULATE TOTAL MARKS OF THE STUDENT
    print("total marks =",total)                                                            #FOR PRINTING TOTAL MARKS OF THE STUDENT
    percentage = total / 5                                                                  #TO CALCULATE TOTAL PERCENTAGE OF THE STUDENT
    print("Percentage =", percentage)                                                       #FOR PRINTING TOTAL PERCENTAGE OF THE STUDENT
    if percentage >= 70.0:                                                                  #USE OF CONDITIONAL STATEMENT TO CALCULATE GRADE
      print("your grade is A")                                                              #IF PERCENTAGE IS MORE THAN 70% DISPLAY GRADE A
    elif percentage <= 60.0:
      print("your grade is B")                                                              #IF PERCENTAGE IS BETWEEN 70% AND 60% DISPLAY GRADE B
    else:
      print("your grade is C")                                                              #IF PERCENTAGE IS BELOW 60% DISPLAY GRADE C

obj=reportcard()
obj.examination("Harleen",1,80,80,80,80,80)                                                 #USE OF INPUT FUNCTION TO ADD VALUES WHICH WERE VALUELIZED ABOVE
obj.result()                                                                                #USE OF OUTPUT FUNCTION TO DISPLAY VALUES,TOTAL,PERCENTAGE AND GRADE