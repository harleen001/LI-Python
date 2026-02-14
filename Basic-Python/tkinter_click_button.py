from tkinter import *
root = Tk()
root.title("Harleen Singh")
root.geometry('350x200')
lbl = Label(root, text = "Want to enter?")
lbl.grid()
def clicked():
	lbl.configure(text = "you clicked button")
btn = Button(root, text = "Click me" ,fg = "blue", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()
