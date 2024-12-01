import tkinter as tk
from tkinter import StringVar
import random
import base64

# Root window configuration
root = tk.Tk()
root.geometry("1200x450")  # Adjusted window size for better layout clarity
root.title("Encryption/Decryption with Vigenere Cipher")

# Top frame
top_frame = tk.Frame(root, width=1600, relief=tk.SUNKEN)
top_frame.pack(side=tk.TOP)

title_label = tk.Label(
    top_frame,
    font=("Rockwell", 30, "bold"),  # Updated font size for a cleaner header
    text="Encryption/Decryption with Vigenere Cipher",
    fg="black",
    bd=10,
    anchor="w",
)
title_label.grid(row=0, column=0)

# Left frame
left_frame = tk.Frame(root, width=800, relief=tk.SUNKEN)
left_frame.pack(side=tk.LEFT)

# Variables
msg_var = StringVar()
key_var = StringVar()
mode_var = StringVar()
result_var = StringVar()

# Functions
def encode(key, msg):
    """Encodes the message using Vigenere Cipher."""
    # Optimized encoding logic for clarity and efficiency
    enc = [(chr((ord(msg[i]) + ord(key[i % len(key)])) % 256)) for i in range(len(msg))]
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    """Decodes the encrypted message using Vigenere Cipher."""
    # Optimized decoding logic for clarity and efficiency
    enc = base64.urlsafe_b64decode(enc).decode()
    dec = [chr((256 + ord(enc[i]) - ord(key[i % len(key)])) % 256) for i in range(len(enc))]
    return "".join(dec)

def process_result():
    """Processes the encryption or decryption."""
    msg = msg_var.get()
    key = key_var.get()
    mode = mode_var.get().lower()

    try:
        if mode == "e":
            result_var.set(encode(key, msg))
        elif mode == "d":
            result_var.set(decode(key, msg))
        else:
            result_var.set("Invalid mode! Use 'e' for encrypt or 'd' for decrypt.")
    except Exception as e:
        result_var.set(f"Error: {e}")  # Added error handling for robustness

def reset():
    """Resets all fields."""
    # Reset all input fields and result
    msg_var.set("")
    key_var.set("")
    mode_var.set("")
    result_var.set("")

def exit_app():
    """Exits the application."""
    root.destroy()  # Exits the program safely

# UI Components
def create_label(frame, text, row, column):
    """Creates and places a label."""
    label = tk.Label(
        frame,
        font=("Garamond", 16, "bold"),  # Standardized font across all labels
        text=text,
        bd=16,
        anchor="w",
    )
    label.grid(row=row, column=column)

def create_entry(frame, variable, row, column):
    """Creates and places an entry box."""
    entry = tk.Entry(
        frame,
        font=("Garamond", 16, "bold"),
        textvariable=variable,
        bd=10,
        insertwidth=4,
        bg="powder blue",
        justify="left",
    )
    entry.grid(row=row, column=column)

# Labels and Entries
create_label(left_frame, "Message", 1, 0)
create_entry(left_frame, msg_var, 1, 1)

create_label(left_frame, "Cipher Key", 2, 0)
create_entry(left_frame, key_var, 2, 1)

create_label(left_frame, "Mode (e for encrypt, d for decrypt)", 3, 0)
create_entry(left_frame, mode_var, 3, 1)

create_label(left_frame, "Result", 4, 0)
result_entry = tk.Entry(
    left_frame,
    font=("Garamond", 16, "bold"),
    textvariable=result_var,
    bd=10,
    insertwidth=4,
    bg="powder blue",
    justify="left",
    state="readonly",  # Made the result entry read-only to avoid accidental edits
)
result_entry.grid(row=4, column=1)

# Buttons
tk.Button(
    left_frame,
    text="Show Result",
    font=("Garamond", 16, "bold"),
    bg="powder blue",
    command=process_result,
).grid(row=5, column=1)

tk.Button(
    left_frame,
    text="Reset",
    font=("Garamond", 16, "bold"),
    bg="green",
    command=reset,
).grid(row=5, column=2)

tk.Button(
    left_frame,
    text="Exit",
    font=("Garamond", 16, "bold"),
    bg="red",
    command=exit_app,
).grid(row=5, column=3)

# Keep the window alive
root.mainloop()
