import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq

# Function to handle login
def login():
    # Get the input values
    username = entry_username.get()
    password = entry_password.get()

    # Step 1: Connect to the database
    conn = sq.connect('project_database.db')
    
    # Step 2: Create a cursor object
    cursor = conn.cursor()
    
    # Step 3: Query the database to match the username and password
    cursor.execute('''
    SELECT * FROM admin WHERE username = ? AND password = ?
    ''', (username, password))
    
    # Step 4: Fetch the result
    result = cursor.fetchone()  # This will return None if no match is found
    
    # Step 5: Verify if a match was found
    if result:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

    # Step 6: Close the connection
    conn.close()

# Hover effect function for buttons
def on_enter(e):
    e.widget['background'] = '#000'

def on_leave(e):
    e.widget['background'] = '#a525cc'

# Create the main window
root = tk.Tk()
root.title("Login to Admin")
# icon = tk.PhotoImage(file="")
# root.iconphoto(True, icon)

# Get the screen width and height for dynamic sizing
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to 40% of screen width and 50% of screen height
max_width = int(screen_width)  
max_height = int(screen_height)  
root.geometry(f"{max_width}x{max_height}")
root.configure(bg="#f0f4f7")  # Light gray-blue background

# Frame to hold the form elements with rounded corners, shadow, and padding
frame = tk.Frame(root, bg="#ffffff", bd=4, relief="groove", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=400)

# Title label with enhanced styling
label_title = tk.Label(frame, text="Login To Admin", bg="#ffffff", fg="#333", 
                       font=("Helvetica", 20, "bold"), padx=10, pady=10)
label_title.pack(pady=10)

# Username label with updated font and color
label_username = tk.Label(frame, text="Username", bg="#ffffff", fg="#555555", 
                          font=("Arial", 12, "bold"))
label_username.pack(pady=(5, 2))

# Username entry field with padding and border
entry_username = tk.Entry(frame, width=30, bd=2, relief="solid", font=("Arial", 12))
entry_username.pack(pady=5)

# Password label with updated font and color
label_password = tk.Label(frame, text="Password", bg="#ffffff", fg="#555555", 
                          font=("Arial", 12, "bold"))
label_password.pack(pady=(5, 2))

# Password entry field with asterisks and padding
entry_password = tk.Entry(frame, width=30, bd=2, relief="solid", font=("Arial", 12), show="*")
entry_password.pack(pady=5)

# Forgot details link with blue text, underlined style, and cursor hover effect
forgot_label = tk.Label(frame, text="I Am Farmer", bg="#ffffff", fg="#007bff", 
                        cursor="hand2", font=("Arial", 10, "underline"))
forgot_label.pack(pady=5)

# Remember me checkbox with styled text
remember_var = tk.IntVar()  # Define the remember_var here
remember_check = tk.Checkbutton(frame, text="Remember me", variable=remember_var, 
                                bg="#ffffff", font=("Arial", 10), fg="#333333")
remember_check.pack(pady=(5, 10))

# Sign-in button with hover effect, padding, and styling
sign_in_button = tk.Button(frame, text="Sign In", command=login, bg="#a525cc", fg="white", 
                           width=14, height=2, font=("Arial", 12, "bold"), bd=0, relief="flat", cursor="hand2")
sign_in_button.pack(pady=15)

# Adding hover effects to buttons
sign_in_button.bind("<Enter>", on_enter)
sign_in_button.bind("<Leave>", on_leave)


# Run the application
root.mainloop()
