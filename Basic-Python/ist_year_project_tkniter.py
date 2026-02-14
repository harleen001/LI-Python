from tkinter import *
import sqlite3
from tkinter import messagebox
import re


def clear():
    # clear output area
    #   output.delete(0.0,END)

    entry_Employeename.delete(0, END)
    entry_Employeepassword.delete(0, END)
    entry_Employeecontact.delete(0, END)
    entry_employeeemail.delete(0, END)
    entry_employeeage.delete(0, END)
    # clear checkbox and radio
    checkbox1.set(0)
    checkbox2.set(0)
    checkbox3.set(0)
    employeegender.set(0)


# Callback functions

def checkEmployeename(Employeename):
    if Employeename.isalnum():
        return True
    if Employeename == "":
        return True
    else:
        messemployeeagebox.showwarning("Invalid", "Not allowed " + Employeename[-1])
        return False


"""
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\])    Require that at least one special character appear anywhere in the string
.{8,32}                                      The Employeepassword must be at least 8 characters long, but no more than 32
$                                            Match the end of the string.
"""


def checkEmployeepassword(Employeepassword):
    if len(Employeepassword) <= 20:
        if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))", Employeepassword):
            return True

        messemployeeagebox.showwarning("Invalid", "Enter valid Employeepassword")
        return False
    else:
        messemployeeagebox.showwarning("Invalid", "Length try to exceed")
        return False


def checkEmployeecontact(con):
    if con.isdigit():
        return True
    if len(str(con)) == 0:
        return True


    else:
        messemployeeagebox.showwarning("Invalid", "Invalid Entry")
        return False


def checkemployeeemail(employeeemail):
    if len(employeeemail) > 7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", employeeemail):
            return True


        else:
            messemployeeagebox.showwarning("Alert", "Invalid E-mail enter by user")
            return False
    else:
        messemployeeagebox.showwarning("Alert", "employeeemail length is too small")


# validate all field at submit time
def validations():
    x = y = 0
    if Employeename.get() == "":
        messemployeeagebox.showinfo("Alert", "Enter your Employeename first")
    elif Employeepassword.get() == "":
        messemployeeagebox.showinfo("Alert", "Enter Employeepassword")
    elif Employeecontact.get() == "" or len(Employeecontact.get()) != 10:
        messemployeeagebox.showinfo("Alert", "Enter valid EmployeeEmployeecontact")
    elif employeeemail.get() == "":
        messemployeeagebox.showinfo("Alert", "Enter employeeemail")
    elif employeeage.get() == "":
        messemployeeagebox.showinfo("Alert", "Enter employeeage")
    elif employeegender.get() == 0:
        messemployeeagebox.showinfo("Alert", "Select employeegender")
    elif employeerole.get() == "" or employeerole.get() == "Select your employeerole":
        messemployeeagebox.showinfo("Alert", "Select employeerole")
    elif checkbox1.get() == 0 and checkbox2.get() == 0 :
        messemployeeagebox.showinfo("Alert", "Select languemployeeage")
    elif employeeemail.get() != None and Employeepassword.get() != None:

        x = checkemployeeemail(employeeemail.get())
        y = checkEmployeepassword(Employeepassword.get())
        print(x, y)
    if (x == True) and (y == True):
        employeetype = []
        Employeename1 = Employeename.get()
        pas1 = Employeepassword.get()
        cont1 = Employeecontact.get()
        employeeemail1 = employeeemail.get()
        employeeage1 = employeeage.get()
        gvar = employeegender.get()
        cnt = employeerole.get()
        employeetype = checkbox1.get(), checkbox2.get()
        employeetype = str(employeetype)
        # print(Employeename1,pas1,cont1,employeeemail1,employeeage1,gvar,cnt,employeetype,type(Employeename1),type(pas1),type(cont1),type(employeeemail1),type(employeeage1),type(gvar),type(cnt),type(employeetype))
        # connection with db
        conn = sqlite3.connect('Register1.db')
        with conn:
            cursor = conn.cursor()
            # querries
            cursor.execute('CREATE TABLE IF NOT EXISTS  Registration(Employeename TEXT,Employeepassword TEXT,EmployeeEmployeecontactText,employeeemail TEXT,employeeage Text,\
                                  employeegender Number,employeerole Text,employeetype Text)')
            cursor.execute(
                'INSERT INTO Registration(Employeename,Employeepassword,Employeecontact,employeeemail,employeeage,employeegender,employeerole,employeetype) VALUES(?,?,?,?,?,?,?,?)',
                (Employeename1, pas1, cont1, employeeemail1, employeeage1, gvar, cnt, employeetype))

        conn.commit()


def view():
    lx = [Employeename.get(), "\n", Employeepassword.get(), "\n", Employeecontact.get(), "\n", employeeemail.get(), "\n",
          employeeage.get(), "\n", employeegender.get(), "\n", employeerole.get(), "\n", checkbox1.get(), "\n", checkbox2.get(), "\n",
          checkbox3.get()]
    messemployeeagebox.showinfo("Details", lx
                        )


# GUI

win = Tk()
win.geometry("830x900")
win.title("employeeingress.edu")
win["bg"] = "grey"

# creating data selection variable on gui
Employeename = StringVar()
Employeepassword = StringVar()
Employeecontact= StringVar()
employeeemail = StringVar()
employeeage = StringVar()
employeegender = IntVar()
employeerole = StringVar()
checkbox1 = IntVar()
checkbox2 = IntVar()

# Form Title
label_title = Label(win, text="Welcome To The\nEmployee Ingress Portal", width=50, font=("italic", 20),bg='lightgrey').place(x=10, y=20)

# Create fields
label_Employeename = Label(win, text="Employee Name", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=130)
entry_Employeename = Entry(win, width=20,font=6,textvariable=Employeename)
entry_Employeename.place(x=500, y=130)
validate_Employeename = win.register(checkEmployeename)  # validation register
entry_Employeename.config(validate="key", validatecommand=(validate_Employeename, "%P"))  # validation configure

label_Employeepassword = Label(win, text="Employee Password", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=180)
entry_Employeepassword = Entry(win,width=20,font=6,textvariable=Employeepassword)
entry_Employeepassword.place(x=500, y=180)

label_Employeecontact= Label(win, text="Employee Contact", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=230)
entry_Employeecontact= Entry(win, width=20,font=6, textvariable=Employeecontact)
entry_Employeecontact.place(x=500, y=230)
validate_Employeecontact= win.register(checkEmployeecontact)  # validation register
entry_Employeecontact.config(validate="key", validatecommand=(validate_Employeecontact, "%P"))

label_employeeemail = Label(win, text="Employee Email Id", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=280)
entry_employeeemail = Entry(win, width=20,font=6, textvariable=employeeemail)
entry_employeeemail.place(x=500, y=280)

label_employeeage = Label(win, text="Employee Age", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=330)
entry_employeeage = Spinbox(win, width=19,font=6, textvariable=employeeage, from_=1, to_=150)
entry_employeeage.place(x=500, y=330)

label_employeegender = Label(win, text="Employee Gender", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=380)
g_radio_male = Radiobutton(win, width=5,font=6, text="Male", padx=5, variable=employeegender, value=1).place(x=500, y=380)
g_radio_female = Radiobutton(win, width=5,font=6, text="Female", padx=20, variable=employeegender, value=2).place(x=605, y=380)

label_employeerole = Label(win, text="Employee Role", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=430)
list1 = ['Full Stack Developer', 'Data Scientist', 'DevOps Engineer', 'Java Developer',
         'UI/UX Designer', 'AI/ML Engineer','Data Analyst','System analyst','IT Coordinator','Network Architect',
         'Cloud Infrastructure Architect','Wireless Network Engineer','Database Administrator','Big Data Engineer'];
droplist = OptionMenu(win,employeerole, *list1)
droplist.config(width=17,font=6)
employeerole.set('Select your Role')
droplist.place(x=500, y=430)

label_employeetype = Label(win, text="Employee Type", width=20,height=1,font=6,bg='lightgrey').place(x=100, y=480)
entry_check1 = Checkbutton(win, width=6,font=3, text="Intern", variable=checkbox1).place(x=500, y=480)
entry_check2 = Checkbutton(win, width=8,font=3, text="Full Time", variable=checkbox2).place(x=610, y=480)

Button(win, text='Submit', width=10,height=1,font=6, bg='maroon', fg='white', command=validations).place(x=150, y=560)
Button(win, text='Clear Data', width=10,height=1,font=6, bg='maroon', fg='white', command=clear).place(x=350, y=560)
Button(win, text='Check', width=10,height=1,font=6, bg='maroon', fg='white', command=view).place(x=600, y=560)

win.mainloop()