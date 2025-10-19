import tkinter as tk
from tkinter import *

# Function to convert text to uppercase
def to_uppercase():
    text = input_text.get("1.0", tk.END)
    
    result_text.insert(tk.END, text.upper())

# Function to convert text to lowercase
def to_lowercase():
    text = input_text.get("1.0", tk.END)
    
    result_text.insert(tk.END, text.lower())

# Function to convert text to title case
def to_titlecase():
    text = input_text.get("1.0", tk.END)
    
    result_text.insert(tk.END, text.title())

# Create main window
root = tk.Tk()
root.title("Text Case Converter")
root.geometry("400x400")
root.config(bg="#e8f0fe")

# Title Label
tk.Label(root, text="Text Case Converter", font=("Arial", 16, "bold"), bg="#e8f0fe").pack(pady=10)

# Input Text Box
tk.Label(root, text="Enter your text below:", bg="#e8f0fe").pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

# Buttons for conversion
btn_frame = tk.Frame(root, bg="#e8f0fe")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="UPPERCASE", command=to_uppercase, width=12, bg="#4caf50").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="lowercase", command=to_lowercase, width=12, bg="#2196f3").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Title Case", command=to_titlecase, width=12, bg="#ff9800").grid(row=0, column=2, padx=5)

# Output Text Box
tk.Label(root, text="Converted text:", bg="#e8f0fe").pack()
result_text = tk.Text(root, height=5, width=40, bg="#fff8e1")
result_text.pack(pady=5)

# Run the root
root.mainloop()