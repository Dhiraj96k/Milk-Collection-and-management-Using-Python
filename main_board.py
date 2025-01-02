import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime
import threading  # To ensure database queries do not block the GUI
import subprocess

class MilkManagementApp:
    def __init__(self, root):
        self.root = root
        self.context = {}
        

        # Set up the main window layout
        self.create_mainboard()

    # Helper methods
    def clear_entry(self, entry):
        entry.delete(0, tk.END)

    def insert_into_entry(self, entry, value):
        self.clear_entry(entry)
        entry.insert(0, value)
        
        
    def manage(self):
        subprocess.Popen(["python","add-user.py"])
    
    def report(self):
        subprocess.Popen(["python","pdffile.py"])

    # Fetch details from the database by code
    def fetch_details_by_code(self, code):
        try:
            conn = sqlite3.connect('project_database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name, mobno FROM per_info WHERE code = ?", (code,))
            result = cursor.fetchone()
            conn.close()
            return result
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {e}")
            return None

# Calculate rate based on fat and SNF
    def calculate_rate(self, fat, snf):
        if fat >= 3.0 and snf > 8.0:
            if 3.0 <= fat <= 3.4 and 8.0 < snf <= 8.3:
                return 33
            elif 3.4 < fat <= 3.8 and 8.3 < snf <= 8.7:
                return 35
            elif fat > 3.8 and snf > 8.8:
                return 37
            else:
                return 32  
        elif fat < 3.0 or snf <= 8.0:
            return 30  # Lower rate 
        else:
            return 0  



    # code entry change
    def on_code_entry_change(self, event=None):
        code = self.context['code_entry'].get()
        if code.isdigit():
            result = self.fetch_details_by_code(int(code))
            if result:
                self.insert_into_entry(self.context['name_entry'], result[0])
                self.insert_into_entry(self.context['mobno_entry'], result[1])
            else:
                messagebox.showerror("Error", f"No data found for code: {code}")
                self.clear_entry(self.context['name_entry'])
                self.clear_entry(self.context['mobno_entry'])
        else:
            self.clear_entry(self.context['name_entry'])
            self.clear_entry(self.context['mobno_entry'])

    #calculate total
    def calculate_total(self, event=None):
        try:
            fat = float(self.context['fat_entry'].get())
            snf = float(self.context['snf_entry'].get())
            liter = float(self.context['liter_entry'].get())
            
            if not (0 < fat < 10 and 0 < snf < 10):
                messagebox.showwarning("Warning", "Fat and SNF values should be between 0 and 10.")
                return
            
            rate = self.calculate_rate(fat, snf)
            if rate == 0:
                messagebox.showwarning("Warning", "Fat and SNF values are out of valid range.")
                self.insert_into_entry(self.context['rate_entry'], "0")
            else:
                self.insert_into_entry(self.context['rate_entry'], str(rate))
            
            total_amount = liter * rate
            self.insert_into_entry(self.context['total_entry'], f"{total_amount:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
            self.clear_entry(self.context['rate_entry'])
            self.clear_entry(self.context['total_entry'])

    # current time period (AM/PM)
    def get_time_period(self):
        current_hour = datetime.now().hour
        return "AM" if current_hour < 12 else "PM"

    # Function to check if a record already exists for the same date and time period
    def check_if_record_exists(self, code, current_date, time_period):
        try:
            conn = sqlite3.connect('project_database.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(*) FROM milk_info
                              WHERE code = ? AND date = ? AND time_period = ?""", (code, current_date, time_period))
            count = cursor.fetchone()[0]
            conn.close()
            return count > 0
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error checking existing record: {e}")
            return False

    # Add record method
    def add_record(self, treeview):
        code = self.context['code_entry'].get()
        liter = self.context['liter_entry'].get()
        fat = self.context['fat_entry'].get()
        snf = self.context['snf_entry'].get()
        rate = self.context['rate_entry'].get()
        total_amount = self.context['total_entry'].get()

        if not (code and liter and fat and snf and rate and total_amount):
            messagebox.showerror("Input Error", "All fields must be filled to add a record.")
            return

        current_date = datetime.now().strftime('%Y-%m-%d')
        time_period = self.get_time_period()

        if self.check_if_record_exists(code, current_date, time_period):
            messagebox.showerror("Error", f"Record for code {code} already exists for {time_period} today.")
            return

        threading.Thread(target=self.insert_record, args=(code, liter, fat, snf, rate, total_amount, current_date, time_period, treeview)).start()

    # Insert record into the database
    def insert_record(self, code, liter, fat, snf, rate, total_amount, current_date, time_period, treeview):
        try:
            conn = sqlite3.connect('project_database.db')
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO milk_info (code, liter, fat, snf, rate, amount, date, time_period)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                           (code, liter, fat, snf, rate, total_amount, current_date, time_period))
            conn.commit()
            conn.close()

            self.update_milk_table(treeview)
            messagebox.showinfo("Success", "Record added successfully!")

            for entry in self.context.values():
                self.clear_entry(entry)
            
            self.context['code_entry'].focus()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error while adding record: {e}")

        # Update milk table with latest records
    def update_milk_table(self, treeview):
        try:
            # Get the current date
            current_date = datetime.now().strftime('%Y-%m-%d')

            # Connect to the database
            conn = sqlite3.connect('project_database.db')
            cursor = conn.cursor()

            # Modify the query to select records for the current date
            cursor.execute("""SELECT code, liter, fat, snf, rate, amount, date 
                            FROM milk_info WHERE date = ?""", (current_date,))
            rows = cursor.fetchall()
            conn.close()

            # Clear the existing rows in the treeview
            for row in treeview.get_children():
                treeview.delete(row)

            # Insert the new rows into the treeview
            for row in rows:
                treeview.insert('', 'end', values=row)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error while fetching data for table: {e}")

        # Update the selected record
    def on_update_button_click(self, treeview):
        # Get the selected record in the treeview
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a record to update.")
            return

        # Extract the original code from the selected record
        original_code = treeview.item(selected_item[0])["values"][0]

        try:
            # Fetch updated values from entry fields
            updated_values = {
                "liter": self.context['liter_entry'].get(),
                "fat": self.context['fat_entry'].get(),
                "snf": self.context['snf_entry'].get(),
                "rate": self.context['rate_entry'].get(),
                "amount": self.context['total_entry'].get()
            }

            # Validate that all values are filled
            if not all(updated_values.values()):
                raise ValueError("All fields must be filled.")

            # Convert values to appropriate types
            updated_values = {key: float(value) for key, value in updated_values.items()}

            # Connect to the database and update the record
            conn = sqlite3.connect('project_database.db')
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE milk_info 
                SET liter = ?, fat = ?, snf = ?, rate = ?, amount = ?
                WHERE code = ?""",
                (updated_values["liter"], updated_values["fat"], updated_values["snf"],
                updated_values["rate"], updated_values["amount"], original_code)
            )
            conn.commit()
            conn.close()

            # Refresh the treeview
            self.update_milk_table(treeview)

            # Notify the user of success
            messagebox.showinfo("Success", "Record updated successfully!")

            # Clear the entry fields after updating
            for entry in self.context.values():
                self.clear_entry(entry)
            self.context['code_entry'].focus()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating record: {e}")
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid input: {ve}")

        # Exit application with confirmation
        def exit_application(self):
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.root.destroy()

    def create_mainboard(self):
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        top_banner = tk.Frame(self.root, bg="yellow", height=60)
        top_banner.pack(fill="x")
        tk.Label(top_banner, text="Kamdhenu Dhudh Sankal Kendra", font=("Arial", 20, "bold"), bg="yellow").pack(side="left", padx=20)
        time_label = tk.Label(top_banner, font=("Arial", 12, "bold"), bg="yellow", fg="red")
        time_label.pack(side="right", padx=20)

        def update_time():
            time_label.config(text=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
            self.root.after(1000, update_time)
        update_time()

        left_frame = tk.Frame(self.root, padx=20, pady=10)
        left_frame.pack(side="left", fill="y")
        
        labels = ["Code", "Name", "Mob.No", "Liter", "Fat", "SNF", "Rate", "Total Amount"]
        for i, text in enumerate(labels):
            tk.Label(left_frame, text=text, font=("Arial", 12, "bold")).grid(row=i, column=0, pady=5, sticky="w")

        # Entry widgets
        self.context['code_entry'] = tk.Entry(left_frame, font=("Arial", 12))
        self.context['name_entry'] = tk.Entry(left_frame, font=("Arial", 12))
        self.context['mobno_entry'] = tk.Entry(left_frame, font=("Arial", 12))
        self.context['liter_entry'] = tk.Entry(left_frame, font=("Arial", 12), bg="#FFDDDD")
        self.context['fat_entry'] = tk.Entry(left_frame, font=("Arial", 12), bg="#FFDDDD")
        self.context['snf_entry'] = tk.Entry(left_frame, font=("Arial", 12), bg="#FFDDDD")
        self.context['rate_entry'] = tk.Entry(left_frame, font=("Arial", 12))
        self.context['total_entry'] = tk.Entry(left_frame, font=("Arial", 12))
        
        entries = list(self.context.values())
        for i, entry in enumerate(entries):
            entry.grid(row=i, column=1, pady=5, padx=5)
        
        # Create buttons with equal width and height
        button_width = 17
        button_height = 2
        tk.Button(left_frame, text="Add", font=("Arial", 12, "bold"), bg="green", fg="white", 
                width=button_width, height=button_height, command=lambda: self.add_record(treeview)).grid(row=8, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(left_frame, text="Update", font=("Arial", 12, "bold"), bg="blue", fg="white", 
                width=button_width, height=button_height, command=lambda: self.on_update_button_click(treeview)).grid(row=8, column=1, padx=10, pady=5, sticky="ew")

        tk.Button(left_frame, text="Manage", font=("Arial", 12, "bold"), bg="green", fg="white", 
                width=button_width, height=button_height, command=lambda: self.manage()).grid(row=9, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(left_frame, text="Report", font=("Arial", 12, "bold"), bg="blue", fg="white", 
                width=button_width, height=button_height, command=lambda: self.report()).grid(row=9, column=1, padx=10, pady=5, sticky="ew")

        
        right_frame = tk.Frame(self.root, padx=20, pady=10)
        right_frame.pack(side="right", fill="y")

        treeview = ttk.Treeview(right_frame, columns=("Code", "Liter", "Fat", "SNF", "Rate", "Total Amount", "Date"), show="headings")
        treeview.heading("Code", text="Code")
        treeview.heading("Liter", text="Liter")
        treeview.heading("Fat", text="Fat")
        treeview.heading("SNF", text="SNF")
        treeview.heading("Rate", text="Rate")
        treeview.heading("Total Amount", text="Total Amount")
        treeview.heading("Date", text="Date")

        treeview.column("Code", width=100)
        treeview.column("Liter", width=100)
        treeview.column("Fat", width=100)
        treeview.column("SNF", width=100)
        treeview.column("Rate", width=100)
        treeview.column("Total Amount", width=150)
        treeview.column("Date", width=150)

        treeview.pack(fill="both", expand=True)

        # Update table with data from the database
        self.update_milk_table(treeview)

        # Bindings
        self.context['code_entry'].bind("<Return>", self.on_code_entry_change)
        self.context['snf_entry'].bind("<Return>", self.calculate_total)

# Create Tkinter root window and start the application
root = tk.Tk()
root.title("Milk Collection System")
app = MilkManagementApp(root)
root.mainloop()
