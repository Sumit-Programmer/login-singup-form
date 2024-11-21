import customtkinter as ctk
from tkinter import messagebox
import json

def login():
    # Function to load library data from JSON file
    def load_library():
        try:
            with open("data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    # Function to save library data to JSON file
    def save_library(library):
        with open("data.json", "w") as f:
            json.dump(library, f, indent=4)

    # Function to save student details
    def check_details():
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()

        library = load_library()
        for student in library:
            if student["name"] == name and student["email"] == email and student["password"] == password:
                messagebox.showinfo("Success", "Login Successful.")
                return
        messagebox.showerror("Error", "Invalid credentials.")


    # Main GUI setup
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue, "dark-purple", "dark-yellow"

    root = ctk.CTk()
    root.geometry("450x500")
    root.resizable(False, False)
    root.title("Login")

    frame_main = ctk.CTkFrame(root)
    frame_main.pack(pady=0, padx=0, fill="both", expand=True)

    # Add widgets to the frame
    label_title = ctk.CTkLabel(frame_main, text="Login", font=("Bold Arial", 30), text_color="red")
    label_title.pack(pady=10)

    label_name = ctk.CTkLabel(frame_main, text="Name", font=("Bold Arial", 15))
    label_name.pack(padx=10)
    entry_name = ctk.CTkEntry(frame_main, placeholder_text="Enter your name")
    entry_name.pack(pady=10)

    label_email = ctk.CTkLabel(frame_main, text="Email")
    label_email.pack(pady=10)
    entry_email = ctk.CTkEntry(frame_main, placeholder_text="Enter your email")
    entry_email.pack(pady=10)

    label_password = ctk.CTkLabel(frame_main, text="Password")
    label_password.pack(pady=10)
    entry_password = ctk.CTkEntry(frame_main, show="• ", placeholder_text="Enter your password")
    entry_password.pack(pady=10)

    button_submit = ctk.CTkButton(frame_main, text="Login", command=check_details, fg_color="#16e", text_color="black", hover_color="#5dc")
    button_submit.pack(pady=10)



# Main event loop
    root.protocol("WM_DELETE_WINDOW")
    root.mainloop()
