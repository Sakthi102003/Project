import tkinter as tk
from tkinter import ttk

from cryptography.fernet import Fernet


# Generate a random AES key
def generate_aes_key():
    return Fernet.generate_key()

# Initialize the cipher suite with a given key
def initialize_cipher_suite(key):
    return Fernet(key)

# Encrypt text using AES-CBC
def encrypt_text(text, cipher_suite):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# Decrypt text using AES-CBC
def decrypt_text(encrypted_text, cipher_suite):
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text.decode()

# Function to perform encryption and update the result container
def perform_encryption():
    input_text = e1.get("1.0", "end-1c")
    aes_key = generate_aes_key()
    cipher_suite = initialize_cipher_suite(aes_key)
    encrypted_text = encrypt_text(input_text, cipher_suite)
    
    # Insert the encrypted text and AES key into the Text widget
    e2.delete("1.0", "end")
    e2.insert("1.0", f"Encrypted Text: {encrypted_text.decode()}\nAES Key: {aes_key.decode()}")

# Function to perform decryption and update the result container
def perform_decryption():
    input_text = e1.get("1.0", "end-1c")
    aes_key = input_text.split("\n")[-1].split(": ")[1]
    cipher_suite = initialize_cipher_suite(aes_key.encode())
    encrypted_text = input_text.split("\n")[0].split(": ")[1].encode()
    decrypted_text = decrypt_text(encrypted_text, cipher_suite)
    
    # Insert the decrypted text into the Text widget
    e2.delete("1.0", "end")
    e2.insert("1.0", f"Decrypted Text: {decrypted_text}")

# Function to clear the input and output fields
def clear():
    e1.delete("1.0", "end")
    e2.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Text Encryption")

# Create a label for the title
l = tk.Label(root, text="Text Encryption and Decryption", font="Calibri 14 bold")
l.pack(padx=10, pady=7)

# Create a label frame for the input field
lf1 = tk.LabelFrame(root, text="Enter Plain Text or Encrypted Text")
lf1.pack(padx=5, pady=5)

# Create a frame for the input field and scrollbar
f1 = tk.Frame(lf1)
f1.pack(padx=5, pady=5)

# Create a scrollbar for the input field
s1 = tk.Scrollbar(f1)
s1.pack(side="right", fill="y")

# Create a text widget for the input field
e1 = tk.Text(f1, height=10, font="Calibri 12")
e1.pack(side="left", fill="both")
s1.config(command=e1.yview)
e1.config(yscrollcommand=s1.set)

# Create a frame for the buttons
f2 = tk.Frame(root)
f2.pack(padx=10, pady=5)

# Create buttons for encryption, decryption, and clearing
b1 = tk.Button(f2, text="Encrypt", command=perform_encryption)
b1.pack(padx=10, pady=5, side="left")
b2 = tk.Button(f2, text="Decrypt", command=perform_decryption)
b2.pack(padx=10, pady=5, side="left")
b3 = tk.Button(f2, text="Clear", command=clear)
b3.pack(padx=10, pady=5)

# Create a label frame for the output field
lf2 = tk.LabelFrame(root, text="Output")
lf2.pack(padx=5, pady=5)

# Create a frame for the output field and scrollbar
f3 = tk.Frame(lf2)
f3.pack(padx=5, pady=5)

# Create a scrollbar for the output field
s2 = tk.Scrollbar(f3)
s2.pack(side="right", fill="y")

# Create a text widget for the output field
e2 = tk.Text(f3, height=10, font="Calibri 12")
e2.pack(side="left", fill="both")
s2.config(command=e2.yview)
e2.config(yscrollcommand=s2.set)

# Start the GUI main loop
root.mainloop()