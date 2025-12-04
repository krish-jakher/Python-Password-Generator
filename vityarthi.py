import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    # 1. Get Password Length from GUI Input
    try:
        length_input = length_entry.get()
        length = int(length_input)
        
        if length < 4:
            messagebox.showwarning("Invalid Input", "Length must be at least 4.")
            return
            
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    # 2. Define Character Sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    character_pool = lower_case + upper_case + digits + symbols
    
    # 3. Generating the Password
    password_list = []
    
    # Add Mandatory Characters
    password_list.append(secrets.choice(lower_case))
    password_list.append(secrets.choice(upper_case))
    password_list.append(secrets.choice(digits))
    password_list.append(secrets.choice(symbols))

    remaining_length = length - len(password_list)

    for i in range(remaining_length):
        password_list.append(secrets.choice(character_pool))

    # Shuffle
    secrets.SystemRandom().shuffle(password_list)
    final_password = "".join(password_list)
    
    # 4. Display Result in GUI
    result_var.set(final_password)
    status_label.config(text="Password Generated!", fg="green")

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update() # Keeps the clipboard current
        status_label.config(text="Copied to Clipboard!", fg="blue")
    else:
        status_label.config(text="Generate a password first.", fg="red")

# --- GUI SETUP ---

# Create main window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Length Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Password Length:", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
length_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
length_entry.insert(0, "12") # Default value
length_entry.pack(side=tk.LEFT)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, 
                         font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
generate_btn.pack(pady=15)

# Result Display (Entry widget allowing copy/paste)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Courier New", 14), 
                        state="readonly", width=25, justify="center")
result_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 10))
copy_btn.pack(pady=5)

# Status Label (for messages like "Copied!")
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

# Run the App
root.mainloop()
