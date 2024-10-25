import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Milk Collection and Management")

# Automatically detect screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width)
window_height = int(screen_height)

# Set the size of the window
root.geometry(f"{window_width}x{window_height}")
root.config(bg="#f0f0f0")  # Set background color of the root window

# Create a frame for the header (which contains the image and the label)
header_frame = tk.Frame(root, bd=5, relief=tk.RAISED, bg="#4CAF50")
header_frame.pack(fill=tk.X, pady=10)

# Load and place the image on the left
image = Image.open("cow-img.jpeg")
image = image.resize((80, 80), Image.Resampling.LANCZOS)  # Resize image to fit next to label
photo = ImageTk.PhotoImage(image)

# Create a frame for the image and label to center them
center_frame = tk.Frame(header_frame, bg="#4CAF50")
center_frame.pack(side=tk.TOP, padx=20, pady=10)

# Add the image
image_label = tk.Label(center_frame, image=photo, bg="#4CAF50")
image_label.pack(side=tk.LEFT)

# Create the title label next to the image
header_label = tk.Label(center_frame, text="Milk Collection and Management", 
                        font=("Arial", 30, "bold"), fg="white", bg="#4CAF50")
header_label.pack(side=tk.LEFT, padx=20)

# Create two frames to divide the screen into Admin and User login sections
left_frame = tk.Frame(root, width=window_width//2, height=window_height, bd=5, relief=tk.GROOVE, bg="#e0f7fa")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

right_frame = tk.Frame(root, width=window_width//2, height=window_height, bd=5, relief=tk.GROOVE, bg="#ffe0b2")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Admin Login Section ---
admin_label = tk.Label(left_frame, text="Admin Login", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40")
admin_label.pack(pady=30)

# Username label and entry
admin_username_label = tk.Label(left_frame, text="Username", font=("Arial", 16), bg="#e0f7fa")
admin_username_label.pack(pady=10)
admin_username_entry = tk.Entry(left_frame, font=("Arial", 16), bd=3)
admin_username_entry.pack(pady=10)

# Password label and entry
admin_password_label = tk.Label(left_frame, text="Password", font=("Arial", 16), bg="#e0f7fa")
admin_password_label.pack(pady=10)
admin_password_entry = tk.Entry(left_frame, font=("Arial", 16), bd=3, show="*")
admin_password_entry.pack(pady=10)

# Admin Login button
admin_login_button = tk.Button(left_frame, text="Login", font=("Arial", 16, "bold"), bg="#009688", fg="white", bd=3)
admin_login_button.pack(pady=30)

# --- User Login Section ---
user_label = tk.Label(right_frame, text="User Login", font=("Arial", 24, "bold"), bg="#ffe0b2", fg="#bf360c")
user_label.pack(pady=30)

# Mobile number label and entry
user_mobile_label = tk.Label(right_frame, text="Mobile Number", font=("Arial", 16), bg="#ffe0b2")
user_mobile_label.pack(pady=10)
user_mobile_entry = tk.Entry(right_frame, font=("Arial", 16), bd=3)
user_mobile_entry.pack(pady=10)

# Code label and entry
user_code_label = tk.Label(right_frame, text="Code", font=("Arial", 16), bg="#ffe0b2")
user_code_label.pack(pady=10)
user_code_entry = tk.Entry(right_frame, font=("Arial", 16), bd=3)
user_code_entry.pack(pady=10)

# User Login button
user_login_button = tk.Button(right_frame, text="Login", font=("Arial", 16, "bold"), bg="#FF5722", fg="white", bd=3)
user_login_button.pack(pady=30)

# Start the Tkinter event loop
root.mainloop()
