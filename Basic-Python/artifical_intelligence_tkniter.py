import tkinter as tk
from tkinter import messagebox
class LoginPage(tk.Frame):
    def init(self, master):
        tk.Frame.init(self, master)
        self.pack(side="top", fill="both", expand=True)
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

    # Replace this with your own authentication logic
        if username == "admin" and password == "1234":
            self.master.switch_frame(WelcomePage)
        else:
            messagebox.showerror("Error", "Incorrect username or password.")
class WelcomePage(tk.Frame):
    def init(self, master):
        tk.Frame.init(self, master)
        self.pack(side="top", fill="both", expand=True)
        self.welcome_label = tk.Label(self, text="Welcome to the employee portal!")
        self.welcome_label.pack()

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack()


    def logout(self):
        self.master.switch_frame(LoginPage)
class MainApplication(tk.Tk):
    def init(self, *args, **kwargs):
        tk.Tk.init(self, *args, **kwargs)
        self.geometry("300x200")
        self.title("Employee Login")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [LoginPage, WelcomePage]:
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

                self.switch_frame(LoginPage)


    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
if username == "main":
    app = MainApplication()
    app.mainloop()