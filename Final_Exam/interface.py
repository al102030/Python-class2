import tkinter as tk
from tkinter import messagebox, filedialog
from user import Student, Teacher
from database import Database
import json
import csv


class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('User Management')
        self.master.geometry("800x350")

        self.db = Database()

        # Input fields
        self.name_label = tk.Label(master, text='Name:', pady=20)
        self.name_label.grid(row=0, column=0, sticky='e')
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.family_label = tk.Label(master, text='Family:')
        self.family_label.grid(row=1, column=0, sticky='e')
        self.family_entry = tk.Entry(master)
        self.family_entry.grid(row=1, column=1)

        self.age_label = tk.Label(master, text='Age:')
        self.age_label.grid(row=2, column=0, sticky='e')
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=2, column=1)

        self.email_label = tk.Label(master, text='Email:')
        self.email_label.grid(row=3, column=0, sticky='e')
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=3, column=1)

        # Position selection
        self.position_label = tk.Label(master, text='Position:')
        self.position_label.grid(row=4, column=0, sticky='e')

        self.position_var = tk.StringVar()
        self.position_var.set('Student')

        self.student_radio = tk.Radiobutton(
            master, text='Student', variable=self.position_var, value='Student')
        self.student_radio.grid(row=4, column=1, sticky='w')

        self.teacher_radio = tk.Radiobutton(
            master, text='Teacher', variable=self.position_var, value='Teacher')
        self.teacher_radio.grid(row=4, column=1, sticky='e')

        # Buttons
        self.add_button = tk.Button(
            master, text='Add User', command=self.add_user)
        self.add_button.grid(row=5, column=1)

        self.export_json_button = tk.Button(
            master, text='Export JSON', command=self.export_json)
        self.export_json_button.grid(row=5, column=2)

        self.export_csv_button = tk.Button(
            master, text='Export CSV', command=self.export_csv)
        self.export_csv_button.grid(row=5, column=3)

        # Listboxes
        self.student_label = tk.Label(master, text='Students:')
        self.student_label.grid(row=0, column=3)
        self.student_listbox = tk.Listbox(master)
        self.student_listbox.grid(row=1, column=3, rowspan=4)

        self.teacher_listbox = tk.Listbox(master)
        self.teacher_listbox.grid(row=1, column=4, rowspan=4)
        self.teacher_label = tk.Label(master, text='Teachers:')
        self.teacher_label.grid(row=0, column=4)

        self.refresh_lists()

    def add_user(self):
        name = self.name_entry.get()
        family = self.family_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        position = self.position_var.get()

        if not name or not family or not age or not email:
            messagebox.showerror('Error', 'Please fill all fields.')
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror('Error', 'Age must be an integer.')
            return

        if position == 'Student':
            user = Student(name, family, age, email)
            self.db.insert_student(user)
        else:
            user = Teacher(name, family, age, email)
            self.db.insert_teacher(user)

        self.name_entry.delete(0, tk.END)
        self.family_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        self.refresh_lists()

    def refresh_lists(self):
        # Clear listboxes
        self.student_listbox.delete(0, tk.END)
        self.teacher_listbox.delete(0, tk.END)

        # Get data from database
        students = self.db.get_students()
        teachers = self.db.get_teachers()

        # Populate listboxes
        for student in students:
            self.student_listbox.insert(
                tk.END, f"{student[0]} {student[1]}, Age: {student[2]}, Email: {student[3]}")

        for teacher in teachers:
            self.teacher_listbox.insert(
                tk.END, f"{teacher[0]} {teacher[1]}, Age: {teacher[2]}, Email: {teacher[3]}")

    def export_json(self):
        # Export students and teachers to JSON
        students = self.db.get_students()
        teachers = self.db.get_teachers()

        students_list = [{'name': s[0], 'family': s[1],
                          'age': s[2], 'email': s[3]} for s in students]
        teachers_list = [{'name': t[0], 'family': t[1],
                          'age': t[2], 'email': t[3]} for t in teachers]

        data = {'students': students_list, 'teachers': teachers_list}

        file_path = filedialog.asksaveasfilename(
            defaultextension='.json', filetypes=[('JSON files', '*.json')])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo('Success', 'Data exported to JSON file.')

    def export_csv(self):
        # Export students and teachers to CSV
        students = self.db.get_students()
        teachers = self.db.get_teachers()

        # Export students
        file_path_students = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[
                                                          ('CSV files', '*.csv')], title='Save Students CSV')
        if file_path_students:
            with open(file_path_students, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Family', 'Age', 'Email'])
                for s in students:
                    writer.writerow(s)
            messagebox.showinfo(
                'Success', 'Students data exported to CSV file.')

        # Export teachers
        file_path_teachers = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[
                                                          ('CSV files', '*.csv')], title='Save Teachers CSV')
        if file_path_teachers:
            with open(file_path_teachers, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Family', 'Age', 'Email'])
                for t in teachers:
                    writer.writerow(t)
            messagebox.showinfo(
                'Success', 'Teachers data exported to CSV file.')

    def on_closing(self):
        self.db.close()
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
