import os
from tkinter import filedialog
import customtkinter as ctk
import subprocess

app = ctk.CTk()
app.title("Hugo Page Generator")
app.resizable(False, False)
app.geometry("700x500")

# ------------------------ Global Variables -------------------------------------------------
Folder_PATH = ""


# ------------------------ PATH SELECTOR STARTS -------------------------------------------------


def select_path():
    """
    :return: Set Folder Path in Folder_textbox
    """
    Folder_textbox.delete("0.0", "end")
    global Folder_PATH
    Folder_PATH = filedialog.askdirectory()
    os.chdir(Folder_PATH)
    Folder_textbox.insert(index=0.0, text=Folder_PATH)
    update_archtype_list()


Folder_label = ctk.CTkLabel(app, text="Select Hugo Project")
Folder_label.place(relx=0.01, rely=0.04)
Folder_textbox = ctk.CTkTextbox(app, width=550, height=30)
Folder_textbox.place(relx=0.01, rely=0.1)
Browse_path_button = ctk.CTkButton(app, text="Browse...", height=30, command=select_path)
Browse_path_button.place(relx=0.799, rely=0.1)

# ------------------------ PATH SELECTOR ENDS -------------------------------------------------

# ------------------------ Archetypes SELECTOR Start -------------------------------------------------
Archtype_label = ctk.CTkLabel(app, text="Select Archtype")
Archtype_label.place(relx=0.01, rely=0.17)


def option_menu_callback(choice):
    ArchType_menu.set(choice)
    print("option menu dropdown clicked:", choice)


def get_archtypes():
    try:
        global Folder_PATH
        Archtype_Path = Folder_PATH+"/archetypes"
        print(Archtype_Path)
        archtype_list = os.listdir(Archtype_Path)
        archtype_list_no_ext = [os.path.splitext(filename)[0] for filename in archtype_list]
        print(archtype_list)
        return archtype_list_no_ext
    except FileNotFoundError:
        return ["None"]


def update_archtype_list():
    current_list = get_archtypes()
    ArchType_menu.configure(values=current_list)


ArchType_menu = ctk.CTkOptionMenu(app, values=get_archtypes(), command=option_menu_callback)
ArchType_menu.place(relx=0.01, rely=0.23)
ArchType_menu.set("default")

# ------------------------ ArchType SELECTOR ENDS -------------------------------------------------


app.mainloop()
