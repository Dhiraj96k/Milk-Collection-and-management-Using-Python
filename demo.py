import tkinter as tk

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


# Start the Tkinter event loop
root.mainloop()
