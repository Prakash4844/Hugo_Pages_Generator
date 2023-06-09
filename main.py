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
Page_count = 0


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
    """
    Set Archtype in ArchType_menu

    :param choice:
    :return: none
    """
    ArchType_menu.set(choice)


def get_archtypes():
    """
    get list of archtypes in archetypes folder of Hugo Project

    :return: list of archtypes in archetypes folder of Hugo Project
    :return: None if archetypes folder not found
    """
    try:
        global Folder_PATH
        Archtype_Path = Folder_PATH + "/archetypes"
        archtype_list = os.listdir(Archtype_Path)
        archtype_list_no_ext = [os.path.splitext(filename)[0] for filename in archtype_list]
        return archtype_list_no_ext
    except FileNotFoundError:
        return ["None"]


def update_archtype_list():
    """
    Update ArchType_menu with list of archtypes in archetypes folder of Hugo Project
    :return: none
    """
    current_list = get_archtypes()
    ArchType_menu.configure(values=current_list)


ArchType_menu = ctk.CTkOptionMenu(app, values=get_archtypes(), command=option_menu_callback)
ArchType_menu.place(relx=0.01, rely=0.23)
ArchType_menu.set("default")

# ------------------------ ArchType SELECTOR ENDS -------------------------------------------------

# ------------------------ Custom PATH STARTS -----------------------------------------------------

Custom_Path_label = ctk.CTkLabel(app, text="Put custom path here(optional) Ex: /blog/")
Custom_Path_label.place(relx=0.01, rely=0.3)
Custom_Path_textbox = ctk.CTkTextbox(app, width=250, height=30)
Custom_Path_textbox.place(relx=0.01, rely=0.36)


# ------------------------ Custom PATH ENDS -------------------------------------------------------

# ------------------------ Page count STARTS -------------------------------------------------------

def page_slider_event(value):
    """
    Set Page_count in Page_count_label
    :param value: value of page count slider
    :return: none
    """
    global Page_count
    Page_count = int(value)
    Page_count_label.configure(text="Number of Pages: " + str(Page_count) + "\n(Note: this will create page with "
                                                                            "archtype names)")


Page_count_label = ctk.CTkLabel(app, text="Number of Pages: 1 \n(Note: this will create page with archtype names)")
Page_count_label.place(relx=0.01, rely=0.45)
page_count_slider = ctk.CTkSlider(app, width=250, from_=1, to=100, orientation="horizontal", command=page_slider_event)
page_count_slider.set(1)
page_count_slider.place(relx=0.03, rely=0.52)

# ------------------------ Page count Ends -------------------------------------------------------

# ------------------------ Page List Starts ------------------------------------------------------

Page_list_label = ctk.CTkLabel(app, text="Page List Put each page name in new line \n(Use this or Page count)")
Page_list_label.place(relx=0.01, rely=0.6)
Page_list_textbox = ctk.CTkTextbox(app, width=250, height=120, activate_scrollbars=True)
Page_list_textbox.place(relx=0.01, rely=0.67)

# ------------------------ Page List Ends --------------------------------------------------------


app.mainloop()
