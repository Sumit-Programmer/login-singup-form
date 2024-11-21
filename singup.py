import customtkinter as ctk
from tkinter import messagebox
import json
from login import login

# Function to load library data from JSON file
def load_library():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save library data to JSON file
def save_library(library):
    with open("data.json", "w") as f:
        json.dump(library, f, indent=4)

# Function to save student details
def save_details():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    elif len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return
    elif not name or not email or not password:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return
    
    student_data = {
        "name": name,
        "email": email,
        "password": password,
    }
    
    library = load_library()
    if library is None:
        library = []  # Ensure library is a list if loading fails
    
    library.append(student_data)
    save_library(library)
    
    messagebox.showinfo("Success", "Student information was saved successfully.")
    
    entry_name.delete(0, ctk.END)
    entry_email.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)
    entry_confirm_password.delete(0, ctk.END)


# Main GUI setup
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.geometry("500x550")
root.resizable(False, False)
root.title("Sing Up")

# Create the main frame
frame_main = ctk.CTkFrame(root)
frame_main.pack(pady=0, padx=0, fill="both", expand=True)

# Create the widgets
label_title = ctk.CTkLabel(frame_main, text="Sing Up", font=("Bold Arial", 30), text_color="red")
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

label_confirm_password = ctk.CTkLabel(frame_main, text="Confirm Password")
label_confirm_password.pack(pady=10)
entry_confirm_password = ctk.CTkEntry(frame_main, show="• ", placeholder_text="Confirm your password")
entry_confirm_password.pack(pady=10)

button_submit = ctk.CTkButton(frame_main, text="Sing Up", command=save_details, fg_color="#ecf", text_color="black", hover_color="#5cc")
button_submit.pack(pady=10)

login_button = ctk.CTkButton(frame_main, text="Login", command=login, fg_color="#5cf", text_color="black", hover_color="#5cc")
login_button.place(relx=0.8, rely=0.05, anchor="center")

# Main event loop
root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()

