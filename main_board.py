import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# Function to fetch details from the database by code
def fetch_details_by_code(code):
    """Fetch the name and mobno from per_info based on the code."""
    # Connect to the database
    conn = sqlite3.connect('project_database.db')
    cursor = conn.cursor()
    
    # Query the database for the given code
    cursor.execute("SELECT name, mobno FROM per_info WHERE code = ?", (code,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    if result:
        return result  # Return the name and mobno
    else:
        return None  # Return None if no record is found

# Event handler for when the code entry field loses focus or Enter is pressed
def on_code_entry_change(event=None):
    """Function to handle code entry change event when focus is lost or Enter is pressed."""
    code = code_entry.get()
    
    if code.isdigit():  # Ensure the entered code is a number
        # Fetch name and mobno from the database based on code
        result = fetch_details_by_code(int(code))
        
        if result:
            # Update the name and mobno fields with the fetched data
            name_entry.delete(0, tk.END)
            name_entry.insert(0, result[0])
            
            mobno_entry.delete(0, tk.END)
            mobno_entry.insert(0, result[1])
        else:
            # If no data is found for the entered code, show an error message
            messagebox.showerror("Error", f"No data found for code: {code}")
            name_entry.delete(0, tk.END)
            mobno_entry.delete(0, tk.END)
    else:
        # Clear the fields if the code is not a valid number
        name_entry.delete(0, tk.END)
        mobno_entry.delete(0, tk.END)

# Function to create the main board (GUI)
def create_mainboard(root):
    # Set the geometry of the main window to full screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    # Top banner with title and time
    top_banner = tk.Frame(root, bg="yellow", height=60)
    top_banner.pack(fill="x")
    title_label = tk.Label(top_banner, text="THE HINDU DHUDH SANKULAN KENDRA", font=("Arial", 20, "bold"), bg="yellow")
    title_label.pack(pady=10, side="left", padx=20)

    time_label = tk.Label(top_banner, font=("Arial", 12, "bold"), bg="yellow", fg="red")
    time_label.pack(pady=10, side="right", padx=20)

    # Left side - Data Entry Section
    left_frame = tk.Frame(root, padx=20, pady=10)
    left_frame.pack(side="left", fill="y", expand=False)

    # Code Entry Field
    tk.Label(left_frame, text="Code", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5, sticky="w")
    global code_entry  # Make code_entry global so it can be accessed in other functions
    code_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    code_entry.grid(row=0, column=1, pady=5, padx=5)
    code_entry.bind("<Return>", on_code_entry_change)  # Bind Enter key to call the function
    
    # Name Entry Field
    tk.Label(left_frame, text="Name", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=5, sticky="w")
    global name_entry  # Make name_entry global
    name_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    name_entry.grid(row=1, column=1, pady=5, padx=5)
    
    # Mobile Number Entry Field
    tk.Label(left_frame, text="Mob.No", font=("Arial", 12, "bold")).grid(row=2, column=0, pady=5, sticky="w")
    global mobno_entry  # Make mobno_entry global
    mobno_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    mobno_entry.grid(row=2, column=1, pady=5, padx=5)
    
    # Literature Section
    tk.Label(left_frame, text="Liter", font=("Arial", 12, "bold")).grid(row=3, column=0, pady=5, sticky="w")
    liter_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    liter_entry.grid(row=3, column=1, pady=5, padx=5)
    
    # Fat Section
    tk.Label(left_frame, text="Fat", font=("Arial", 12, "bold")).grid(row=4, column=0, pady=5, sticky="w")
    fat_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    fat_entry.grid(row=4, column=1, pady=5, padx=5)

    # SNF Section
    tk.Label(left_frame, text="SNF", font=("Arial", 12, "bold")).grid(row=5, column=0, pady=5, sticky="w")
    snf_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    snf_entry.grid(row=5, column=1, pady=5, padx=5)
    
    # Amount Section
    tk.Label(left_frame, text="Amount", font=("Arial", 12, "bold")).grid(row=6, column=0, pady=5, sticky="w")
    amount_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    amount_entry.grid(row=6, column=1, pady=5, padx=5)

    # Average Quantity, Fat, SNF, Rate Section
    tk.Label(left_frame, text="AVG. Qty", font=("Arial", 12, "bold")).grid(row=3, column=2, pady=5, padx=10, sticky="w")
    avg_qty_entry = tk.Entry(left_frame, width=10, font=("Arial", 12))
    avg_qty_entry.grid(row=3, column=3, pady=5, padx=5)

    tk.Label(left_frame, text="AVG. Fat", font=("Arial", 12, "bold")).grid(row=4, column=2, pady=5, padx=10, sticky="w")
    avg_fat_entry = tk.Entry(left_frame, width=10, font=("Arial", 12))
    avg_fat_entry.grid(row=4, column=3, pady=5, padx=5)

    tk.Label(left_frame, text="AVG. SNF", font=("Arial", 12, "bold")).grid(row=5, column=2, pady=5, padx=10, sticky="w")
    avg_snf_entry = tk.Entry(left_frame, width=10, font=("Arial", 12))
    avg_snf_entry.grid(row=5, column=3, pady=5, padx=5)

    tk.Label(left_frame, text="Rate", font=("Arial", 12, "bold")).grid(row=6, column=2, pady=5, padx=10, sticky="w")
    rate_entry = tk.Entry(left_frame, width=10, font=("Arial", 12))
    rate_entry.grid(row=6, column=3, pady=5, padx=5)

    # Button section
    button_frame = tk.Frame(root, padx=10, pady=10)
    button_frame.pack(side="left", fill="y", expand=False)
    tk.Button(button_frame, text="OK", font=("Arial", 12, "bold"), width=10, height=2).pack(pady=10)
    tk.Button(button_frame, text="Setting", font=("Arial", 12, "bold"), width=10, height=2).pack(pady=10)
    tk.Button(button_frame, text="Close", font=("Arial", 12, "bold"), width=10, height=2, command=root.quit).pack(pady=10)

    # Right side - Summary and List
    right_frame = tk.Frame(root, padx=10, pady=10)
    right_frame.pack(side="left", fill="both", expand=True)

    # Summary table
    summary_label = tk.Label(right_frame, text="Summary", font=("Arial", 14, "bold"))
    summary_label.pack(anchor="w")
    columns = ("Milk", "Member", "Liter", "Fat", "SNF", "Amount", "Sales")
    summary_table = ttk.Treeview(right_frame, columns=columns, show="headings", height=2)
    for col in columns:
        summary_table.heading(col, text=col)
        summary_table.column(col, anchor="center", width=100)
    summary_table.pack(fill="x", pady=10)

    # List table
    list_label = tk.Label(right_frame, text="List", font=("Arial", 14, "bold"))
    list_label.pack(anchor="w")
    list_columns = ("Code", "Liter", "Fat", "SNF", "Rate", "Amount")
    list_table = ttk.Treeview(right_frame, columns=list_columns, show="headings", height=4)
    for col in list_columns:
        list_table.heading(col, text=col)
        list_table.column(col, anchor="center", width=80)
    list_table.pack(fill="x", pady=10)

    # Previous Day's Collection table
    prev_day_label = tk.Label(right_frame, text="Previous Day's Milk Collection", font=("Arial", 12, "bold"), bg="#FFCCCC")
    prev_day_label.pack(fill="x", pady=5)
    prev_day_columns = ("Date", "Liter", "Fat", "SNF", "Rate", "Amount")
    prev_day_table = ttk.Treeview(right_frame, columns=prev_day_columns, show="headings", height=2)
    for col in prev_day_columns:
        prev_day_table.heading(col, text=col)
        prev_day_table.column(col, anchor="center", width=100)
    prev_day_table.pack(fill="x", pady=10)

    # Function to update time
    def update_time():
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        time_label.config(text=current_time)
        root.after(1000, update_time)  # Update every 1 second

    # Update time initially
    update_time()

# Initialize and run the main application window
root = tk.Tk()
root.title("Milk Collection System")
create_mainboard(root)
root.mainloop()
