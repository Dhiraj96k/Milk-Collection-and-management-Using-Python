import tkinter as tk
from tkinter import messagebox

# Function to be called when button is clicked
def on_button_click():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Demo")

# Set the size of the window
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Welcome to Tkinter!", font=("Helvetica", 14))
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
