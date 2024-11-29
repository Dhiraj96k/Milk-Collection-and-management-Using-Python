import tkinter as tk
from tkinter import ttk

class MilkManagementApp:
    def __init__(self, root):
        # Initialize main window
        self.root = root
        self.root.title("Milk Management and Collection")
        self.root.geometry("1000x700")

        # Default values
        self.avg_milk_amount = 250000  
        self.avg_quality = "Excellent"
        self.avg_rate_amount = 300000  

        # Sidebar visibility state
        self.is_sidebar_visible = False

        # Create the UI components
        self.create_sidebar()
        self.create_dashboard()

    def format_currency(self, amount):
        return f"₹{amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ",")

    def toggle_sidebar(self):
        if self.is_sidebar_visible:
            self.sidebar_frame.pack_forget()  # Hide the sidebar
            self.is_sidebar_visible = False
        else:
            self.sidebar_frame.pack(side="top", fill="x")  # Show the sidebar
            self.sidebar_frame.lift()  # Bring the sidebar to the front
            self.sidebar_frame.after(10, self.slide_down)  # Start the slide down animation
            self.is_sidebar_visible = True

    def slide_down(self):
        if self.sidebar_frame.winfo_height() < 200:  # Limit height for the sliding effect
            self.sidebar_frame.config(height=self.sidebar_frame.winfo_height() + 5)
            self.sidebar_frame.after(10, self.slide_down)
        else:
            self.sidebar_frame.config(height=tk.WINCH)

    def button_action(self, message):
        print(message)

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self.root, width=200, bg="#333", relief="raised", height=0)
        toggle_button = tk.Button(self.root, text="☰ Menu", command=self.toggle_sidebar, font=("Arial", 12, "bold"), bg="#333", fg="white", relief="flat")
        toggle_button.pack(side="top", anchor="nw", padx=5, pady=5)

        menu_label = tk.Label(self.sidebar_frame, text="Menu", bg="#333", fg="white", font=("Arial", 14, "bold"))
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

        for icon_text, message in buttons:
            btn = tk.Button(self.sidebar_frame, text=icon_text, bg="#444", fg="white", font=("Arial", 12), relief="flat", anchor="w", padx=20,
                            command=lambda msg=message: self.button_action(msg))
            btn.pack(fill="x", pady=2)

    def create_dashboard(self):
        # Dashboard area
        self.dashboard_frame = tk.Frame(self.root, bg="white")
        self.dashboard_frame.pack(fill="both", expand=True)

        # Dashboard title
        dashboard_title = tk.Label(self.dashboard_frame, text="Milk Management and Collection", font=("Arial", 24, "bold"), bg="white", fg="#333")
        dashboard_title.pack(pady=20)

        # Information blocks in the middle
        info_frame = tk.Frame(self.dashboard_frame, bg="white")
        info_frame.pack(pady=20)

        # Create info blocks
        self.create_info_block(info_frame, "Avg Milk", self.format_currency(self.avg_milk_amount), "#4CAF50")
        self.create_info_block(info_frame, "Avg Quality", self.avg_quality, "#2196F3")
        self.create_info_block(info_frame, "Avg Rates", self.format_currency(self.avg_rate_amount), "#FF5722")

        # Centered Table section at the bottom
        table_container = tk.Frame(self.dashboard_frame, bg="white")
        table_container.pack(pady=20, fill="both", expand=True)

        table_label = tk.Label(table_container, text="Milk Collection Data", font=("Arial", 16), bg="white")
        table_label.pack(pady=5)

        # Table setup using Treeview with centered values
        columns = ("Date", "Quality", "Quantity", "Rate")
        self.table = ttk.Treeview(table_container, columns=columns, show="headings", height=4, style="Custom.Treeview")

        # Configure table columns with center alignment
        for col in columns:
            self.table.heading(col, text=col, anchor="center")
            self.table.column(col, anchor="center", width=150)  # Set width for each column as well

        # Style configuration for Treeview to make it look like Excel
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 10), rowheight=25)
        style.configure("Custom.Treeview.Heading", font=("Arial", 11, "bold"), background="#f4f4f4")
        style.map("Custom.Treeview", background=[("selected", "#cce5ff")])

        # Alternating row colors
        self.table.tag_configure("evenrow", background="#f2f2f2")
        self.table.tag_configure("oddrow", background="white")

        # Insert sample data
        sample_data = [
            ("2024-10-01", "Good", self.format_currency(150000), self.format_currency(180000)),
            ("2024-10-02", "Excellent", self.format_currency(170000), self.format_currency(190000)),
            ("2024-10-03", "Fair", self.format_currency(130000), self.format_currency(170000)),
            ("2024-10-04", "Good", self.format_currency(150000), self.format_currency(160000)),
        ]
        for i, row in enumerate(sample_data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.table.insert("", "end", values=row, tags=(tag,))

        self.table.pack(fill="both", expand=True)

    def create_info_block(self, parent, title, number, color):
        frame = tk.Frame(parent, bg=color, width=250, height=150)  # Increased size of the blocks
        frame.pack_propagate(False)  # Prevent resizing to fit content
        frame.pack(side="left", padx=10, pady=10)

        title_label = tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg=color, fg="white")
        title_label.pack(pady=10)  # Added padding to separate title from number

        number_label = tk.Label(frame, text=number, font=("Arial", 24, "bold"), bg=color, fg="white")
        number_label.pack(expand=True)  # Center the number by expanding it

# Main execution
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()

    # Create an instance of the MilkManagementApp
    app = MilkManagementApp(root)

    # Start the Tkinter event loop to run the application
    root.mainloop()
