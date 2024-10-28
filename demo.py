import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
import sqlite3 as sq
from PIL import Image, ImageTk

def main_panel():
    main = tk.Tk()
    main.title("Farmer Login")
    # Get the screen width and height for dynamic sizing
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    # Set the window size to 40% of screen width and 50% of screen height
    max_width = int(screen_width)  
    max_height = int(screen_height)  
    main.geometry(f"{max_width}x{max_height}")
    main.configure(bg="#00ff00")
    
    main.mainloop()

def farmer_login():
    # Destroy the main window
    root.destroy()

    # Predefined OTP for demonstration purposes
    correct_otp = "123456"

    # Create a new window for farmer login
    farmer = tk.Tk()
    farmer.title("Farmer Login")

    # Screen dimensions for dynamic sizing
    screen_width = farmer.winfo_screenwidth()
    screen_height = farmer.winfo_screenheight()

    # Set window size and position it in the center of the screen
    window_width = int(screen_width * 0.4)
    window_height = int(screen_height * 0.5)
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    farmer.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    farmer.configure(bg="#e9eff5")

    # Custom font
    title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
    label_font = tkFont.Font(family="Helvetica", size=12)
    entry_font = tkFont.Font(family="Helvetica", size=11)

    # Frame for styling the login form
    frame = tk.Frame(farmer, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title label with styling
    tk.Label(frame, text="Farmer Login", font=title_font, bg="#ffffff", fg="#333333").grid(row=0, column=0, columnspan=3, pady=(0, 20))

    # Mobile number label and entry
    tk.Label(frame, text="Mobile Number:", font=label_font, bg="#ffffff").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    mobile_entry = tk.Entry(frame, font=entry_font, width=25, bd=1, relief="solid")
    mobile_entry.grid(row=1, column=1, padx=5, pady=8)

    # Code label and entry
    tk.Label(frame, text="Code:", font=label_font, bg="#ffffff").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    code_entry = tk.Entry(frame, font=entry_font, width=25, bd=1, relief="solid")
    code_entry.grid(row=2, column=1, padx=5, pady=8)

    # OTP label and entry
    tk.Label(frame, text="OTP:", font=label_font, bg="#ffffff").grid(row=3, column=0, sticky="e", padx=10, pady=8)
    otp_entry = tk.Entry(frame, font=entry_font, width=15, bd=1, relief="solid")
    otp_entry.grid(row=3, column=1, sticky="w", padx=5, pady=8)

    # "Send OTP" button with flexible placement
    send_otp_button = tk.Button(
        frame, text="Send OTP", font=("Helvetica", 10), width=10,
        bg="#007BFF", fg="white", relief="solid", bd=1, cursor="hand2",
        activebackground="#0056b3"
    )
    # Place the "Send OTP" button next to the OTP entry field; adjust x, y as needed for custom positioning
    send_otp_button.place(x=330, y=130)  # Adjust x and y for desired position

    # Email label and entry
    tk.Label(frame, text="Email:", font=label_font, bg="#ffffff").grid(row=4, column=0, sticky="e", padx=10, pady=8)
    email_entry = tk.Entry(frame, font=entry_font, width=25, bd=1, relief="solid")
    email_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=8)

    # Function to verify OTP and handle login
    def verify_login():
        entered_otp = otp_entry.get()
        if entered_otp == correct_otp:
            messagebox.showinfo("Success", "Login successful!")
            # Code for the next window or dashboard goes here
        else:
            messagebox.showerror("Error", "OTP does not match or user not found.")

    # Custom-styled Login button
    login_button = tk.Button(
        frame, text="Login", font=("Helvetica", 12), command=verify_login,
        width=20, bg="#4CAF50", fg="white", relief="solid", bd=1, cursor="hand2", activebackground="#45a049"
    )
    login_button.grid(row=5, column=0, columnspan=3, pady=(20, 0))

    # Decorative elements
    header_frame = tk.Frame(farmer, bg="#4CAF50", height=20)
    header_frame.pack(fill="x", side="top")
    footer_frame = tk.Frame(farmer, bg="#4CAF50", height=20)
    footer_frame.pack(fill="x", side="bottom")

    farmer.mainloop()

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
        root.destroy()
        main_panel()
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
icon = ImageTk.PhotoImage(Image.open("cow-img.jpeg"))
root.iconphoto(True, icon)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
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
forgot_button = tk.Button(frame, text="I Am Farmer", bg="#ffffff", fg="#007bff",
                          cursor="hand2", font=("Arial", 10, "underline"),
                          command=farmer_login, borderwidth=0)
forgot_button.pack(pady=5)

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
