import sqlite3
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta

def generate_pdf():
    code = entry_code.get().strip()  # Get the code entered by the user
    start_date = entry_start_date.get_date().strftime('%Y-%m-%d') if entry_start_date.get() else None
    end_date = entry_end_date.get_date().strftime('%Y-%m-%d') if entry_end_date.get() else None

    if not start_date or not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')

    try:
        conn = sqlite3.connect('project_database.db')  
        cursor = conn.cursor()

        if code:
            cursor.execute("SELECT name, mobno FROM per_info WHERE code = ?", (code,))
            personal_info = cursor.fetchone()
            if not personal_info:
                messagebox.showinfo("No Data", f"No person found with code {code}.")
                return
            name, mobno = personal_info
        else:
            name, mobno = "All Records", "N/A"

        if code:
            query = """
                SELECT code, liter, fat, snf, amount, rate, date 
                FROM milk_info 
                WHERE code = ? AND date BETWEEN ? AND ?
                ORDER BY date
            """
            cursor.execute(query, (code, start_date, end_date))
        else:
            query = """
                SELECT code, liter, fat, snf, amount, rate, date 
                FROM milk_info 
                WHERE date BETWEEN ? AND ?
                ORDER BY code, date
            """
            cursor.execute(query, (start_date, end_date))

        milk_info = cursor.fetchall()
        if not milk_info:
            messagebox.showinfo("No Data", "No milk records found for the specified criteria.")
            return

    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return
    finally:
        conn.close()

    current_date = datetime.now().strftime('%Y-%m-%d')
    pdf_name = f"Milk_Report_{code if code else 'All'}_{current_date}.pdf"

    try:
        pdf = canvas.Canvas(pdf_name)

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 800, "Kamdhenu Dhudh Sankal Kendra")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(450, 800, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        pdf.drawString(450, 785, f"Time: {datetime.now().strftime('%H:%M:%S')}")

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, 750, f"Code: {code if code else 'All'}")
        pdf.drawString(50, 730, f"Name: {name}")
        pdf.drawString(50, 710, f"Mobile: {mobno}")

        pdf.setFont("Helvetica-Bold", 10)
        headers = ["Code", "Liter", "Fat", "SNF", "Amount", "Rate", "Date"]
        x_positions = [50, 100, 150, 200, 250, 300, 350]
        y_position = 680
        for idx, header in enumerate(headers):
            pdf.drawString(x_positions[idx], y_position, header)

        pdf.setFont("Helvetica", 10)
        y_position -= 20
        total_liter = 0
        total_amount = 0
        total_rate = 0

        for record in milk_info:
            code_data, liter, fat, snf, amount, rate, date = record
            total_liter += liter
            total_amount += amount
            total_rate += rate

            pdf.drawString(x_positions[0], y_position, str(code_data))
            pdf.drawString(x_positions[1], y_position, str(liter))
            pdf.drawString(x_positions[2], y_position, f"{fat:.1f}")
            pdf.drawString(x_positions[3], y_position, f"{snf:.1f}")
            pdf.drawString(x_positions[4], y_position, f"{amount}")
            pdf.drawString(x_positions[5], y_position, f"{rate}")
            pdf.drawString(x_positions[6], y_position, str(date))
            y_position -= 20

            if y_position < 50:  
                pdf.showPage()
                y_position = 750
                pdf.setFont("Helvetica-Bold", 10)
                for idx, header in enumerate(headers):
                    pdf.drawString(x_positions[idx], y_position, header)
                y_position -= 20

        avg_rate = total_rate / len(milk_info) if milk_info else 0
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y_position - 20, f"Total Liter: {total_liter}")
        pdf.drawString(50, y_position - 40, f"Total Amount: {total_amount}")
        pdf.drawString(50, y_position - 60, f"Average Rate: {avg_rate:.2f}")

        pdf.save()
        messagebox.showinfo("Success", f"PDF generated successfully: {pdf_name}\nLocation: Current Directory")
    except Exception as e:
        messagebox.showerror("PDF Error", f"Error: {e}")

# GUI Setup
root = Tk()
root.title("Milk Center Report Generator")
root.geometry("400x500")

Label(root, text="Kamdhenu Dhudh Sankal Kendra Report Generator", font=("Helvetica", 16)).pack(pady=20)
Label(root, text="Enter Code (Leave blank for all):", font=("Helvetica", 12)).pack(pady=5)
entry_code = Entry(root, font=("Helvetica", 12))
entry_code.pack(pady=5)

Label(root, text="Start Date:", font=("Helvetica", 12)).pack(pady=5)
entry_start_date = DateEntry(root, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
entry_start_date.pack(pady=5)

Label(root, text="End Date:", font=("Helvetica", 12)).pack(pady=5)
entry_end_date = DateEntry(root, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
entry_end_date.pack(pady=5)

Button(root, text="Generate PDF", command=generate_pdf, font=("Helvetica", 12), bg="blue", fg="white").pack(pady=20)

root.mainloop()
