import tkinter as tk
from tkinter import ttk
from datetime import datetime

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

    name_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    code_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    mob_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))
    liter_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    fat_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    snf_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), bg="#FFDDDD")
    amount_entry = tk.Entry(left_frame, width=20, font=("Arial", 12))

    # Labels and Entry widgets
    entries = [
        ("Name", name_entry),
        ("Code", code_entry),
        ("Mob.No", mob_entry),
        ("Liter", liter_entry),
        ("Fat", fat_entry),
        ("SNF", snf_entry),
        ("Amount", amount_entry)
    ]
    for i, (label, entry) in enumerate(entries):
        tk.Label(left_frame, text=label, font=("Arial", 12, "bold")).grid(row=i, column=0, pady=5, sticky="w")
        entry.grid(row=i, column=1, pady=5, padx=5)

    # Additional average and rate section
    avg_entries = [
        ("AVG. Qty", "Liter"),
        ("AVG. Fat", "Fat"),
        ("AVG. SNF", "SNF"),
        ("Rate", "Rate")
    ]
    for i, (label, entry) in enumerate(avg_entries, start=3):
        tk.Label(left_frame, text=label, font=("Arial", 12, "bold")).grid(row=i, column=2, pady=5, padx=10, sticky="w")
        avg_entry = tk.Entry(left_frame, width=10, font=("Arial", 12))
        avg_entry.grid(row=i, column=3, pady=5, padx=5)

    # Button section
    def on_ok_button_click():
        # Get data from the entries and insert it into the list table
        member_data = (name_entry.get(), code_entry.get(), mob_entry.get(), liter_entry.get(), fat_entry.get(), snf_entry.get(), amount_entry.get())
        list_table.insert("", "end", values=member_data)
        # Optionally, clear the entries after submitting
        for entry in [name_entry, code_entry, mob_entry, liter_entry, fat_entry, snf_entry, amount_entry]:
            entry.delete(0, tk.END)

    def on_setting_button_click():
        show_settings()

    def on_close_button_click():
        root.quit()  # Close the application

    button_frame = tk.Frame(root, padx=10, pady=10)
    button_frame.pack(side="left", fill="y", expand=False)
    tk.Button(button_frame, text="OK", font=("Arial", 12, "bold"), width=10, height=2, command=on_ok_button_click).pack(pady=10)
    tk.Button(button_frame, text="Setting", font=("Arial", 12, "bold"), width=10, height=2, command=on_setting_button_click).pack(pady=10)
    tk.Button(button_frame, text="Close", font=("Arial", 12, "bold"), width=10, height=2, command=on_close_button_click).pack(pady=10)

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

    # List table with dynamic data population
    list_label = tk.Label(right_frame, text="List", font=("Arial", 14, "bold"))
    list_label.pack(anchor="w")
    list_columns = ("Name", "Code", "Mob.No", "Liter", "Fat", "SNF", "Amount")
    list_table = ttk.Treeview(right_frame, columns=list_columns, show="headings", height=4)
    for col in list_columns:
        list_table.heading(col, text=col)
        list_table.column(col, anchor="center", width=100)
    list_table.pack(fill="x", pady=10)

    # Add scrollbars to the List table
    scrollbar_y = tk.Scrollbar(right_frame, orient="vertical", command=list_table.yview)
    scrollbar_y.pack(side="right", fill="y")
    list_table.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = tk.Scrollbar(right_frame, orient="horizontal", command=list_table.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    list_table.config(xscrollcommand=scrollbar_x.set)

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

    # Settings Window (Popup)
    def show_settings():
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        tk.Label(settings_window, text="Adjust your settings here").pack(pady=10)
        tk.Button(settings_window, text="Close", command=settings_window.destroy).pack(pady=10)

# Initialize and run the main application window
root = tk.Tk()
root.title("Milk Collection System")
create_mainboard(root)
root.mainloop()
