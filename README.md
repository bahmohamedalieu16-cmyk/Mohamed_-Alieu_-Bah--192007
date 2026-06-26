import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime


class GPATracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management & GPA Tracker")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        self.students = []
        self.current_index = -1

        # Title
        title_label = tk.Label(root, text="Student Result Management System",
                               font=("Tahoma", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(root, bg="white", relief=tk.SUNKEN, bd=1)
        input_frame.pack(padx=10, pady=10, fill=tk.X)

        tk.Label(input_frame, text="Student Name:", bg="white").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Student ID:", bg="white").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.id_entry = tk.Entry(input_frame, width=30)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Math Score (0-100):", bg="white").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.math_entry = tk.Entry(input_frame, width=30)
        self.math_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="English Score (0-100):", bg="white").grid(row=3, column=0, sticky=tk.W, padx=5,
                                                                              pady=5)
        self.english_entry = tk.Entry(input_frame, width=30)
        self.english_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Science Score (0-100):", bg="white").grid(row=4, column=0, sticky=tk.W, padx=5,
                                                                              pady=5)
        self.science_entry = tk.Entry(input_frame, width=30)
        self.science_entry.grid(row=4, column=1, padx=5, pady=5)

        # Button Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Student", command=self.add_student,
                  bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Calculate", command=self.calculate_results,
                  bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_form,
                  bg="#FF9800", fg="white", width=15).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Exit", command=root.quit,
                  bg="#f44336", fg="white", width=15).grid(row=0, column=3, padx=5)

        # Output Frame
        output_frame = tk.Frame(root, bg="white", relief=tk.SUNKEN, bd=1)
        output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(output_frame, text="Results:", font=("Tahoma", 10, "bold"), bg="white").pack(anchor=tk.W, padx=5,
                                                                                              pady=5)

        self.output_text = tk.Text(output_frame, height=15, width=70, font=("Tahoma", 9))
        self.output_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.output_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output_text.yview)

    def validate_scores(self, math, english, science):
        """Validate score inputs"""
        try:
            m = float(math)
            e = float(english)
            s = float(science)
            if m < 0 or m > 100 or e < 0 or e > 100 or s < 0 or s > 100:
                return False, None
            return True, (m, e, s)
        except ValueError:
            return False, None

    def calculate_average(self, math, english, science):
        """Calculate average score"""
        return (math + english + science) / 3

    def assign_grade(self, average):
        """Assign letter grade based on average"""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def determine_status(self, average):
        """Determine pass/fail status"""
        if average >= 60:
            return "PASS"
        else:
            return "FAIL"

    def add_student(self):
        """Add student record"""
        name = self.name_entry.get().strip()
        student_id = self.id_entry.get().strip()

        if not name or not student_id:
            messagebox.showerror("Error", "Please enter name and ID")
            return

        valid, scores = self.validate_scores(
            self.math_entry.get(),
            self.english_entry.get(),
            self.science_entry.get()
        )

        if not valid:
            messagebox.showerror("Error", "Scores must be between 0-100")
            return

        math, english, science = scores
        average = self.calculate_average(math, english, science)
        grade = self.assign_grade(average)
        status = self.determine_status(average)

        student = {
            "name": name,
            "id": student_id,
            "math": math,
            "english": english,
            "science": science,
            "average": round(average, 2),
            "grade": grade,
            "status": status
        }

        self.students.append(student)
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        self.clear_form()

    def calculate_results(self):
        """Display all student results"""
        if not self.students:
            messagebox.showwarning("Info", "No students added yet")
            return

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)

        output = "=" * 80 + "\n"
        output += "STUDENT RESULT MANAGEMENT SYSTEM - RESULTS REPORT\n"
        output += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        output += "=" * 80 + "\n\n"

        for student in self.students:
            output += f"Name: {student['name']}\n"
            output += f"ID: {student['id']}\n"
            output += f"Math: {student['math']}, English: {student['english']}, Science: {student['science']}\n"
            output += f"Average: {student['average']}\n"
            output += f"Grade: {student['grade']}\n"
            output += f"Status: {student['status']}\n"
            output += "-" * 80 + "\n"

        self.output_text.insert(tk.END, output)
        self.output_text.config(state=tk.DISABLED)

    def clear_form(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.math_entry.delete(0, tk.END)
        self.english_entry.delete(0, tk.END)
        self.science_entry.delete(0, tk.END)
        self.name_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = GPATracker(root)
    root.mainloop()
