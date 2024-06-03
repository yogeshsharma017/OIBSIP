import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PasswordGen by Yogesh Sharma")
        self.root.geometry("350x250")
        self.root.configure(bg="#f8f9fa")  # Set background color
        
        # Fonts
        self.label_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 10, "bold")
        
        # Labels and Entries
        tk.Label(root, text="Password Length:", bg="#f8f9fa", fg="#333", font=self.label_font).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(root, textvariable=self.length_var, width=5, font=self.label_font)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Checkbox for options
        self.include_upper = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper, bg="#f8f9fa", font=self.label_font).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers, bg="#f8f9fa", font=self.label_font).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special, bg="#f8f9fa", font=self.label_font).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)
        
        # Button to generate password
        self.generate_button = tk.Button(root, text="Generate", command=self.generate_password, bg="black", fg="white", font=self.button_font, relief=tk.FLAT)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        
        # Entry to display generated password
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, state='readonly', font=self.label_font)
        self.password_entry.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        
        # Button to copy password to clipboard
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#28a745", fg="white", font=self.button_font, relief=tk.FLAT)
        self.copy_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
    
    def generate_password(self):
        length = self.length_var.get()
        include_upper = self.include_upper.get()
        include_numbers = self.include_numbers.get()
        include_special = self.include_special.get()
        
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return
        
        characters = string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Ensuring password complexity
        if include_upper:
            password = self.enforce_rule(password, string.ascii_uppercase)
        if include_numbers:
            password = self.enforce_rule(password, string.digits)
        if include_special:
            password = self.enforce_rule(password, string.punctuation)
        
        self.password_var.set(password)
    
    def enforce_rule(self, password, character_set):
        if not any(c in character_set for c in password):
            password = list(password)
            password[random.randint(0, len(password) - 1)] = random.choice(character_set)
            random.shuffle(password)
            password = ''.join(password)
        return password
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
