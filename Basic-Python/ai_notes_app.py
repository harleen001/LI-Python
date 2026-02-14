# Importing necessary libraries
import tkinter as tk
import webbrowser


# Defining the main class
class NotesApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adding a title to the app
        self.title("Notes App")

        # Creating a frame for the app
        frame = tk.Frame(self)
        frame.pack(side="top", fill="both", expand=True)

        # Creating a label for the stream
        stream_label = tk.Label(frame, text="Select your stream:")
        stream_label.pack()

        # Creating a variable to store the stream selection
        self.stream_var = tk.StringVar()
        self.stream_var.set("ENC")


        def show_semesters(self):
            # Showing the semester label and radio buttons
            self.semester_label.pack()
            for button in self.semester_buttons:
                button.pack()

        def show_subjects(self):
            # Showing the subject label and radio buttons
            self.subject_label.pack()
            for button in self.subject_buttons:
                button.pack()

            # Adding a "Open Notes" button to open the notes in Google Drive
            open_button = tk.Button(self, text="Open Notes", command=self.open_notes)
            open_button.pack()

        def open_notes(self):
            # Creating a URL based on the user's selections
            stream = self.stream_var.get()
            semester = self.semester_var.get()
            subject = self.subject_var.get()
            url = f"https://drive.google.com/drive/folders/{stream}-{semester}-{subject}"

            # Opening the URL in a web browser
            webbrowser.open(url)

        # Creating radio buttons for the stream selection
        enc_radio = tk.Radiobutton(frame, text="ENC", variable=self.stream_var, value="ENC",
                                   command=self.show_semesters)
        cse_radio = tk.Radiobutton(frame, text="CSE", variable=self.stream_var, value="CSE",
                                   command=self.show_semesters)
        enc_radio.pack()
        cse_radio.pack()

        # Creating a label for the semester
        self.semester_label = tk.Label(frame, text="Select your semester:")
        self.semester_label.pack_forget()

        # Creating a variable to store the semester selection
        self.semester_var = tk.IntVar()
        self.semester_var.set(1)

        # Creating radio buttons for the semester selection
        self.semester_buttons = []
        for i in range(1, 9):
            self.semester_buttons.append(
                tk.Radiobutton(frame, text=str(i), variable=self.semester_var, value=i, command=self.show_subjects))

        # Creating a label for the subject/book/notes
        self.subject_label = tk.Label(frame, text="Select your subject/book/notes:")
        self.subject_label.pack_forget()

        # Creating a variable to store the subject/book/notes selection
        self.subject_var = tk.StringVar()
        self.subject_var.set("Subject 1")

        # Creating radio buttons for the subject/book/notes selection
        self.subject_buttons = []
        self.subject_buttons.append(
            tk.Radiobutton(frame, text="Subject 1", variable=self.subject_var, value="Subject 1"))
        self.subject_buttons.append(
            tk.Radiobutton(frame, text="Subject 2", variable=self.subject_var, value="Subject 2"))


# Creating an instance of the NotesApp class
app = NotesApp()

# Running the app
app.mainloop()

