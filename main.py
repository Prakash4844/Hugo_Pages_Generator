import os
from tkinter import filedialog
import customtkinter as ctk
from tkterminal import Terminal

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
    Terminal.run_command("cd " + Folder_PATH)
    Folder_textbox.insert(index=0.0, text=Folder_PATH)
    update_archtype_list()
    index_update_archtype_list()


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


def archtype_menu_callback(choice):
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


ArchType_menu = ctk.CTkOptionMenu(app, values=get_archtypes(), command=archtype_menu_callback)
ArchType_menu.place(relx=0.01, rely=0.23)
ArchType_menu.set("default")

# ------------------------ ArchType SELECTOR ENDS -------------------------------------------------

# ------------------------ Custom PATH STARTS -----------------------------------------------------

Custom_Path_label = ctk.CTkLabel(app, text="Put custom path here(optional) Ex: content/blog/")
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
    Page_count_label.configure(text="Number of Pages: " + str(Page_count) +
                                    "\n(Note: this will create page with archtype names)")


Page_count_label = ctk.CTkLabel(app, text="Number of Pages: 1 \n(Note: this will create page with "
                                          "archtype names)")
Page_count_label.place(relx=0.01, rely=0.45)
page_count_slider = ctk.CTkSlider(app, width=250, from_=1, to=500, orientation="horizontal",
                                  command=page_slider_event)
page_count_slider.set(1)
page_count_slider.place(relx=0.03, rely=0.52)

# ------------------------ Page count Ends -------------------------------------------------------

# ------------------------ Page List Starts ------------------------------------------------------

Page_list_label = ctk.CTkLabel(app, text="Page List Put each page name in new line \n"
                                         "(Use this or Page count)")
Page_list_label.place(relx=0.01, rely=0.6)
Page_list_textbox = ctk.CTkTextbox(app, width=250, height=120, activate_scrollbars=True)
Page_list_textbox.place(relx=0.01, rely=0.67)

Page_list_label_precedence = ctk.CTkLabel(app, text="If Specified, This will \n"
                                                    "always overwrite page count slider")
Page_list_label_precedence.place(relx=0.04, rely=0.92)


# ------------------------ Page List Ends --------------------------------------------------------

# ------------------------ Locale Selector Starts -------------------------------------------------


def locale_menu_callback(choice):
    """
    Set Locale in Locale_menu
    :param choice:
    :return: none
    """
    Locale_menu.set(choice)


Locale_label = ctk.CTkLabel(app, text="Select Locale")
Locale_label.place(relx=0.75, rely=0.26)
with open("locale_list", "r") as file:
    locale_list = file.readlines()
    locale_list = [locale.strip() for locale in locale_list]

Locale_menu = ctk.CTkOptionMenu(app, values=locale_list, dynamic_resizing=False, command=locale_menu_callback)
Locale_menu.place(relx=0.75, rely=0.32)
# ------------------------ Locale Selector ends -------------------------------------------------

# ------------------------ Index Archtype terminal Starts -------------------------------------------------
Need_index = ctk.StringVar(value="off")
Need_index_checkbox = ctk.CTkCheckBox(app, text="Need Index?", variable=Need_index, onvalue="on",
                                      offvalue="off")
Need_index_checkbox.place(relx=0.45, rely=0.2)

Need_index_Archtype_label = ctk.CTkLabel(app, text="Select Index Archtype")
Need_index_Archtype_label.place(relx=0.45, rely=0.26)


def index_archtype_menu_callback(choice):
    """
    Set Archtype in ArchType_menu

    :param choice:
    :return: none
    """
    Index_Archtype_menu.set(choice)


def index_get_archtypes():
    """
    get list of archtypes in archetypes folder of Hugo Project

    :return: list of archtypes in archetypes folder of Hugo Project
    :return: None if archetypes folder not found
    """
    try:
        global Folder_PATH
        Index_Archtype_Path = Folder_PATH + "/archetypes"
        Index_archtype_list = os.listdir(Index_Archtype_Path)
        Index_archtype_list_no_ext = [os.path.splitext(filename)[0] for filename in Index_archtype_list]
        return Index_archtype_list_no_ext
    except FileNotFoundError:
        return ["None"]


def index_update_archtype_list():
    """
    Update ArchType_menu with list of archtypes in archetypes folder of Hugo Project
    :return: none
    """
    current_list = get_archtypes()
    Index_Archtype_menu.configure(values=current_list)


Index_Archtype_menu = ctk.CTkOptionMenu(app, values=get_archtypes(), command=index_archtype_menu_callback)
Index_Archtype_menu.place(relx=0.45, rely=0.32)
Index_Archtype_menu.set("Inherited from Archtype")

# ------------------------ Output terminal Starts -------------------------------------------------

Terminal_label = ctk.CTkLabel(app, text="Output Terminal")
Terminal_label.place(relx=0.45, rely=0.4)
Terminal = Terminal(app, relief="sunken", background="#272629", foreground="white", font="Hack 8",
                    height=15, width=60, cursor="arrow", takefocus=False)
Terminal.basename = "Zaphkiel $"
Terminal.place(relx=0.45, rely=0.45)
Terminal.shell = True


# ------------------------ Output terminal Ends ---------------------------------------------------

# ------------------------ Generate Button Starts -------------------------------------------------

def generate():
    """
    Generate pages in Hugo Project
    :return:
    """

    Boilerplate_command = 'hugo new --kind'
    Archtype = ArchType_menu.get()

    Custom_Path = Custom_Path_textbox.get("0.0", "end")
    Custom_Path = Custom_Path.replace("\n", "")
    if Custom_Path == "":
        Custom_Path = "content/"

    locale = Locale_menu.get()

    Page_list = Page_list_textbox.get("0.0", "end")
    Page_list.replace("\n", "")
    Page_list = Page_list.split()
    if not Page_list:
        page_count_slider_value = page_count_slider.get()
        Page_list = [(Archtype + str(i)).strip() + f'.{locale}.md' for i in
                     range(1, int(page_count_slider_value) + 1)]
    else:
        Page_list = [page.strip() + f'.{locale}.md' for page in Page_list]
    if Need_index.get() == "on":
        if Index_Archtype_menu.get() == "Inherited from Archtype":
            Page_list.append(f"_index.{locale}.md")
        else:
            command = Boilerplate_command + " " + \
                      f"{Index_Archtype_menu.get()}" + " " + f'''"{Custom_Path}''' + f'_index.{locale}.md"'
            command.strip()
            Terminal.run_command(command)

    for page in Page_list:
        Custom_page = f'''"{Custom_Path}{page}"'''
        command = Boilerplate_command + " " + Archtype + " " + Custom_page
        command.strip()
        Terminal.run_command(command)

    # Terminal.clear()


Generate_button = ctk.CTkButton(app, text="Generate", font=("Noto Sans", 20), fg_color="#59C837",
                                hover_color="#476A4A", text_color="#000000", command=generate)
Generate_button.place(relx=0.45, rely=0.9)

Exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy, font=("Noto Sans", 20), fg_color="#E9524A",
                            hover_color="#854040")
Exit_button.place(relx=0.77, rely=0.9)

# ------------------------ Generate Button Ends ---------------------------------------------------

# ------------------------ Main Loop Starts -------------------------------------------------------
app.mainloop()
# ------------------------ Main Loop Ends----------------------------------------------------------
