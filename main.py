import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

root = tk.Tk()
root.title("Class Attendance Form App")


def set_arrival_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    arrival_entry.config(state="normal")
    arrival_entry.delete(0, "end")
    arrival_entry.insert(0, current_time)
    arrival_entry.config(state="readonly")

    save_button.config(state="normal")

def set_departure_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    departure_entry.configure(state="normal")
    departure_entry.delete(0,  "end")
    departure_entry.insert(0, current_time)
    departure_entry.configure(state="readonly")

def save_attendance():
     name = name_entry.get().strip()
     surname = surname_entry.get().strip()
     student_class = class_entry.get().strip()
     laptop = laptop_entry.get().strip()
     color = color_entry.get().strip()
     phone = phone_entry.get().strip()
     initials = initials_entry.get().strip()
     arrival = arrival_entry.get().strip()
     departure = departure_entry.get().strip()
     if not name or not surname or not student_class or not laptop or not color or not phone or not initials:
        messagebox.showerror("Missing Information", "Please fill all fields.")

        return

     record = f"{name}, {surname}, {student_class}, {laptop}, {color}, {phone}, {initials}, {arrival}, {departure}\n"

     with open("attendance.csv", "a") as file:
        file.write(record)

     messagebox.showinfo("Success", "Attendance saved successfully!")

     save_button.config(state="disabled")

     name_entry.delete(0, "end")
     surname_entry.delete(0, "end")
     class_entry.delete(0, "end")
     laptop_entry.delete(0, "end")
     color_entry.delete(0, "end")
     phone_entry.delete(0, "end")
     initials_entry.delete(0, "end")

     arrival_entry.config(state="normal")
     arrival_entry.delete(0, "end")
     arrival_entry.config(state="readonly")

     departure_entry.config(state="normal")
     departure_entry.delete(0, "end")
     departure_entry.config(state="readonly")



title_label = ttk.Label(root, text="CLASS ATTENDANCE FORM", font=("Arial", 16, "bold"))
title_label.grid(column=0, row=0, columnspan=3, pady=15)

student_frame = ttk.LabelFrame(root, text="Student Information", padding=10)
student_frame.grid(column=0, row=1, padx=15, pady=10, sticky="ew")


name_label = ttk.Label(student_frame, text="NAME: ")
name_entry = ttk.Entry(student_frame, width=30)
name_label.grid(column=0, row=0, padx=10, pady=5, sticky="e")
name_entry.grid(column=1, row=0, padx=10, pady=5, sticky="w")

surname_label = ttk.Label(student_frame, text="SURNAME: ")
surname_entry = ttk.Entry(student_frame, width=30)
surname_label.grid(column=0, row=1, padx=10, pady=5, sticky="e")
surname_entry.grid(column=1, row=1, padx=10, pady=5, sticky="w")

class_label = ttk.Label(student_frame, text="CLASS: ")
class_entry = ttk.Entry(student_frame, width=30)
class_label.grid(column=0, row=2, padx=10, pady=5, sticky="e")
class_entry.grid(column=1, row=2, padx=10, pady=5, sticky="w")
laptop_label = ttk.Label(student_frame, text="LAPTOP: ")
laptop_entry = ttk.Entry(student_frame, width=30)
laptop_label.grid(column=0, row=3, padx=10, pady=5, sticky="e")
laptop_entry.grid(column=1, row=3, padx=10, pady=5, sticky="w")

color_label = ttk.Label(student_frame, text="COLOR: ")
color_entry = ttk.Entry(student_frame, width=30)
color_label.grid(column=0, row=4, padx=10, pady=5, sticky="e")
color_entry.grid(column=1, row=4, padx=10, pady=5, sticky="w")

phone_label = ttk.Label(student_frame, text="PHONE: ")
phone_entry = ttk.Entry(student_frame, width=30)
phone_label.grid(column=0, row=5, padx=(10, 10), pady=5, sticky="e")
phone_entry.grid(column=1, row=5, padx=10, pady=(5, 5), sticky="w")

initials_label = ttk.Label(student_frame, text="INITIALS: ")
initials_entry = ttk.Entry(student_frame, width=30)
initials_label.grid(column=0, row=6, padx=10, pady=5, sticky="e")
initials_entry.grid(column=1, row=6, padx=10, pady=5, sticky="w")

time_frame = ttk.LabelFrame(root, text="Attendance Times", padding=10)
time_frame.grid(column=0, row=2, padx=15, pady=10, sticky="ew")


arrival_label = ttk.Label(time_frame, text="ARRIVAL TIME: ")
arrival_entry = ttk.Entry(time_frame, width=30)
arrival_entry.config(state="readonly")
arrival_label.grid(column=0, row=0, padx=10, pady=5, sticky="e")
arrival_entry.grid(column=1, row=0, padx=10, pady=5, sticky="w")

departure_label = ttk.Label(time_frame, text="DEPARTURE TIME: ")
departure_entry = ttk.Entry(time_frame, width=30)
departure_entry.configure(state="readonly")
departure_label.grid(column=0,row=1, padx=10, pady=5, sticky="e")
departure_entry.grid(column=1,row=1, padx=10, pady=5, sticky="w")

arrival_button = ttk.Button(time_frame, text="SET ARRIVAL", command=set_arrival_time)
arrival_button.grid(column=2, row=0, padx=10, pady=5)

departure_button = ttk.Button(time_frame, text="SET DEPARTURE", command=set_departure_time)
departure_button.grid(column=2, row=1, padx=10, pady=5)

save_button = ttk.Button(root, text="SAVE ATTENDANCE", command=save_attendance, state="disabled")
save_button.grid(column=0, row=3, columnspan=3, pady=20)

root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()


