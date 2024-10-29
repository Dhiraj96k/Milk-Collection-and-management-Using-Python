import tkinter as tk
from tkinter import ttk

# Function to format numbers in Indian currency style
def format_currency(amount):
    return f"₹{amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ",")

# Increased standard values for the blocks and table data
avg_milk_amount = 250000  # e.g., increased to 2,50,000 L
avg_quality = "Excellent"
avg_rate_amount = 300000  # e.g., increased to ₹3,00,000

# Create the main application window
root = tk.Tk()
root.title("Milk Management and Collection")
root.geometry("1000x700")

# Sidebar visibility state
is_sidebar_visible = False

# Function to toggle the sidebar visibility with sliding effect
def toggle_sidebar():
    global is_sidebar_visible
    if is_sidebar_visible:
        sidebar_frame.pack_forget()  # Hide the sidebar
        is_sidebar_visible = False
    else:
        sidebar_frame.pack(side="top", fill="x")  # Show the sidebar
        sidebar_frame.lift()  # Bring the sidebar to the front
        sidebar_frame.after(10, slide_down)  # Start the slide down animation
        is_sidebar_visible = True

# Function to slide down the sidebar
def slide_down():
    if sidebar_frame.winfo_height() < 200:  # Limit height for the sliding effect
        sidebar_frame.config(height=sidebar_frame.winfo_height() + 5)
        sidebar_frame.after(10, slide_down)
    else:
        sidebar_frame.config(height=tk.WINCHEIGHT)  # Set to desired height after sliding

# Sidebar frame
sidebar_frame = tk.Frame(root, width=200, bg="#333", relief="raised", height=0)
toggle_button = tk.Button(root, text="☰ Menu", command=toggle_sidebar, font=("Arial", 12, "bold"), bg="#333", fg="white", relief="flat")
toggle_button.pack(side="top", anchor="nw", padx=5, pady=5)

menu_label = tk.Label(sidebar_frame, text="Menu", bg="#333", fg="white", font=("Arial", 14, "bold"))
menu_label.pack(pady=10)

# List of menu buttons with examples
buttons = [
    ("🏠 Home", "Welcome to the Milk Management system!"),
    ("👤 User ID", "Your User ID is: 12345"),
    ("🆔 User Code", "Your User Code is: ABCD1234"),
    ("🏠 Address", "Your address is: Milk Lane, Dairy City"),
    ("📝 Feedback", "Thank you for your feedback!"),
    ("🚪 Logout", "You have been logged out successfully.")
]

# Function to handle button clicks
def button_action(message):
    print(message)

for icon_text, message in buttons:
    btn = tk.Button(sidebar_frame, text=icon_text, bg="#444", fg="white", font=("Arial", 12), relief="flat", anchor="w", padx=20,
                    command=lambda msg=message: button_action(msg))
    btn.pack(fill="x", pady=2)

# Dashboard area
dashboard_frame = tk.Frame(root, bg="white")
dashboard_frame.pack(fill="both", expand=True)

# Dashboard title
dashboard_title = tk.Label(dashboard_frame, text="Milk Management and Collection", font=("Arial", 24, "bold"), bg="white", fg="#333")
dashboard_title.pack(pady=20)

# Information blocks in the middle
info_frame = tk.Frame(dashboard_frame, bg="white")
info_frame.pack(pady=20)

# Function to create info blocks with formatted currency
def create_info_block(parent, title, number, color):
    frame = tk.Frame(parent, bg=color, width=250, height=150)  # Increased size of the blocks
    frame.pack_propagate(False)  # Prevent resizing to fit content
    frame.pack(side="left", padx=10, pady=10)
    
    title_label = tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg=color, fg="white")
    title_label.pack(pady=10)  # Added padding to separate title from number
    
    number_label = tk.Label(frame, text=number, font=("Arial", 24, "bold"), bg=color, fg="white")
    number_label.pack(expand=True)  # Center the number by expanding it

# Create the three blocks with increased values
create_info_block(info_frame, "Avg Milk", format_currency(avg_milk_amount), "#4CAF50")
create_info_block(info_frame, "Avg Quality", avg_quality, "#2196F3")
create_info_block(info_frame, "Avg Rates", format_currency(avg_rate_amount), "#FF5722")

# Centered Table section at the bottom
table_container = tk.Frame(dashboard_frame, bg="white")
table_container.pack(pady=20, fill="both", expand=True)

table_label = tk.Label(table_container, text="Milk Collection Data", font=("Arial", 16), bg="white")
table_label.pack(pady=5)

# Table setup using Treeview with centered values
columns = ("Date", "Quality", "Quantity", "Rate")
table = ttk.Treeview(table_container, columns=columns, show="headings", height=4, style="Custom.Treeview")

# Configure table columns with center alignment
for col in columns:
    table.heading(col, text=col, anchor="center")
    table.column(col, anchor="center", width=150)  # Set width for each column as well

# Style configuration for Treeview to make it look like Excel
style = ttk.Style()
style.configure("Custom.Treeview", font=("Arial", 10), rowheight=25)
style.configure("Custom.Treeview.Heading", font=("Arial", 11, "bold"), background="#f4f4f4")
style.map("Custom.Treeview", background=[("selected", "#cce5ff")])

# Alternating row colors
table.tag_configure("evenrow", background="#f2f2f2")
table.tag_configure("oddrow", background="white")

# Insert sample data with formatted currency and alternating row colors
sample_data = [
    ("2024-10-01", "Good", format_currency(150000), format_currency(180000)),  # Increased values
    ("2024-10-02", "Excellent", format_currency(170000), format_currency(190000)),  # Increased values
    ("2024-10-03", "Fair", format_currency(130000), format_currency(170000)),  # Increased values
    ("2024-10-04", "Good", format_currency(150000), format_currency(160000)),  # Increased values
]
for i, row in enumerate(sample_data):
    tag = "evenrow" if i % 2 == 0 else "oddrow"
    table.insert("", "end", values=row, tags=(tag,))

table.pack(fill="both", expand=True)

root.mainloop()
