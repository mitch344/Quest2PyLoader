import os
import subprocess
import threading
import customtkinter as ctk
from tkinter import filedialog, Listbox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def check_device():
    while True:
        result = os.popen('adb devices -l').read()
        if 'device' in result and 'model:Quest' in result:
            status_label.configure(text="Quest Device Connected", text_color="green")
            update_list()
            break

def update_list():
    result = os.popen('adb shell ls /storage/emulated/0/Android/data').read()
    listbox.delete(0, "end")
    for item in result.split('\n'):
        if item.strip():
            listbox.insert("end", item.strip())

def push():
    status_label.configure(text="")
    folder = filedialog.askdirectory()
    if folder:
        status_label.configure(text="Pushing folder...", text_color="blue")
        result = os.system(f'adb push "{folder}" /storage/emulated/0/Android/data')
        if result == 0:
            status_label.configure(text="Folder pushed successfully!", text_color="green")
        else:
            status_label.configure(text="An error occurred while pushing the folder.", text_color="red")
        update_list()

def install():
    status_label.configure(text="")
    file = filedialog.askopenfilename(filetypes=[("APK files", "*.apk")])
    if file:
        status_label.configure(text="Installing APK...", text_color="blue")
        result = subprocess.check_output(f'adb install -r "{file}"', shell=True).decode()
        if "Success" in result:
            status_label.configure(text="APK Installed Successfully!", text_color="green")
        else:
            status_label.configure(text=f"Error: {result}", text_color="red")
        update_list()

def delete():
    selected = listbox.curselection()
    if selected:
        folder_name = listbox.get(selected[0])
        escaped_folder = folder_name.replace(" ", "\\ ")
        status_label.configure(text=f"Deleting {folder_name}...", text_color="blue")
        result = os.system(f'adb shell rm -r "/storage/emulated/0/Android/data/{escaped_folder}"')
        if result == 0:
            status_label.configure(text="Folder deleted successfully!", text_color="green")
        else:
            status_label.configure(text="An error occurred while deleting the folder.", text_color="red")
        update_list()
    else:
        status_label.configure(text="No folder selected.", text_color="red")

def extract():
    selected = listbox.curselection()
    if selected:
        folder_name = listbox.get(selected[0])
        escaped_folder = folder_name.replace(" ", "\\ ")
        local_dir = filedialog.askdirectory()
        if local_dir:
            status_label.configure(text=f"Extracting {folder_name}...", text_color="blue")
            result = os.system(f'adb pull "/storage/emulated/0/Android/data/{escaped_folder}" "{local_dir}"')
            if result == 0:
                status_label.configure(text="Folder extracted successfully!", text_color="green")
            else:
                status_label.configure(text="An error occurred while extracting the folder.", text_color="red")
            update_list()
        else:
            status_label.configure(text="No destination selected.", text_color="red")
    else:
        status_label.configure(text="No folder selected.", text_color="red")

def refresh():
    update_list()

app = ctk.CTk()
app.title("Quest2PyLoader")
app.geometry("600x500")
app.resizable(False, False)


title_label = ctk.CTkLabel(
    app,
    text="Quest2PyLoader",
    font=("Roboto", 24),
    text_color="#1877F2",
)
title_label.pack(pady=10)

status_label = ctk.CTkLabel(
    app,
    text="Connect the Quest Headset and Allow USB Debugging",
    font=("Roboto", 14),
    text_color="red",
)
status_label.pack(pady=10)

listbox_frame = ctk.CTkFrame(app)
listbox_frame.pack(pady=10, fill="both", expand=True, padx=20)

listbox = Listbox(listbox_frame, height=15, font=("Roboto", 12), bg="#2A2A2A", fg="white", bd=0, highlightthickness=0)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = ctk.CTkScrollbar(listbox_frame, command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10, padx=20)

push_button = ctk.CTkButton(button_frame, text="Push Folder", command=push, corner_radius=10, hover_color="#0052cc")
push_button.grid(row=0, column=0, padx=10)

delete_button = ctk.CTkButton(button_frame, text="Delete Folder", command=delete, corner_radius=10, hover_color="#FF3333")
delete_button.grid(row=0, column=1, padx=10)

install_button = ctk.CTkButton(button_frame, text="Install APK", command=install, corner_radius=10, hover_color="#00cc66")
install_button.grid(row=0, column=2, padx=10)

extract_button = ctk.CTkButton(button_frame, text="Extract Folder", command=extract, corner_radius=10, hover_color="#FF9933")
extract_button.grid(row=1, column=0, padx=10, pady=10)

refresh_button = ctk.CTkButton(button_frame, text="Refresh", command=refresh, corner_radius=10, hover_color="#999999")
refresh_button.grid(row=1, column=1, padx=10, pady=10)

thread = threading.Thread(target=check_device, daemon=True)
thread.start()

app.mainloop()
