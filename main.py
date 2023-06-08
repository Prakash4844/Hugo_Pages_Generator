from tkinter import filedialog
import customtkinter as ctk
import subprocess

app = ctk.CTk()
app.title("Hugo Page Generator")
app.resizable(False, False)
app.geometry("700x500")

folder_path = ""


def select_path():
    """
    :return: Set Folder Path in Folder_textbox
    """
    Folder_textbox.delete("0.0", "end")
    Folder_textbox.insert(index=0.0, text=filedialog.askdirectory())


Folder_label = ctk.CTkLabel(app, text="Hugo Project")
Folder_label.place(relx=0.01, rely=0.04)
Folder_textbox = ctk.CTkTextbox(app, width=550, height=30)
Folder_textbox.place(relx=0.01, rely=0.1)
Browse_path_button = ctk.CTkButton(app, text="Browse...", height=30, command=select_path)
Browse_path_button.place(relx=0.799, rely=0.1)

app.mainloop()
