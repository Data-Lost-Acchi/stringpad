from tkinter import *
from tkinter import filedialog

def open_file():
    global TextBox 
    WelcomeLabel.pack_forget()
    OpenUpLabel.pack_forget()
    OpenFileButton.place_forget()
    MakeNewFileButton.place_forget()
    file_path = filedialog.askopenfilename(
        initialdir="",
        title="Select a File to Open",
        filetypes=(
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        )
    )
    
    if file_path:
        print(f"User selected: {file_path}")
        TextBox = Text(window, font=("Times New Roman",12))
        TextBox.insert("1.0", open(file_path, "r").read())
        TextBox.pack(pady=10)
        SaveButton = Button(window, text="Save", font=("Times New Roman",12,"bold"), command=save_file)
        SaveButton.pack(pady=10)
    else:
        WelcomeLabel.pack(pady=20)
        OpenUpLabel.pack(pady=10)
        OpenFileButton.place(anchor="center", relx=0.4, rely=0.5, width=150, height=50)
        MakeNewFileButton.place(anchor="center", relx=0.6, rely=0.5, width=150, height=50)

def new_file():
    global TextBox
  
    WelcomeLabel.pack_forget()
    OpenUpLabel.pack_forget()
    OpenFileButton.place_forget()
    MakeNewFileButton.place_forget()
    TextBox = Text(window, font=("Times New Roman",12))
    TextBox.pack(pady=10)
    SaveButton = Button(window, text="Save", font=("Times New Roman",12,"bold"), command=save_file)
    SaveButton.pack(pady=10)

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save File As"
    )
    
    if file_path:
        with open(file_path, "w") as f:
            f.write(TextBox.get("1.0", "end-1c"))
        print(f"File successfully saved to: {file_path}")

# GUI 
window = Tk()
window.title("String Pad")
window.geometry("800x800")
WelcomeLabel = Label(window, text="Welcome to String Pad", font=("Times New Roman",30,"bold"))
WelcomeLabel.pack(pady=20)
OpenUpLabel = Label(window, text="Open Up a File or Make a New One", font=("Times New Roman",20,"bold"))
OpenUpLabel.pack(pady=10)
OpenFileButton = Button(window, text="Open File", font=("Times New Roman",12,"bold"), command=open_file)
OpenFileButton.place(anchor="center", relx=0.4, rely=0.5, width=150, height=50)
MakeNewFileButton = Button(window, text="Make New File", font=("Times New Roman",12,"bold"), command=new_file)
MakeNewFileButton.place(anchor="center", relx=0.6, rely=0.5, width=150, height=50)

window.mainloop()
