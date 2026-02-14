from tkinter import *
root = Tk()
root.title("Harleen Singh")
root.geometry('350x200')
lbl = Label(root, text = "Want to enter ?")
lbl.grid()
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
def clicked():
	res = "Your text = " + txt.get()
	lbl.configure(text = res)
btn = Button(root, text = "Click here" ,fg = "red", command=clicked)
btn.grid(column=2, row=0)
root.mainloop()
