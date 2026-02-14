from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
win= Tk()
#Set the geometry of tkinter frame
win.geometry("830x900")
win.title("employeeingress.edu")
win["bg"] = "darkgrey"
#Define a new function to open the window
def open_win():
   new= Toplevel(win)
   new.geometry("830x900")
   new.title("New Window")
   new.title("employeeingress.edu")
   new["bg"] = "darkgrey"
   #Create a Label in New window
   Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)


#Create a label
label_title= Label(win, text="Welcome To The\nEmployee Ingress Portal", width=50, font=("Helvetica 17 bold", 20),bg='lightgrey').place(x=10, y=20)
label_turtle=Label(win)

#Create a button to open a New Window
Button(win, text="Open", command=open_win).place(x=200,y=600)
win.mainloop()