import tkinter as tk
from tkinter import messagebox
from time import strftime

root = tk.Tk()
root.title("Digital Clock with Alarm")
root.geometry("500x250")

# Clock Display
clock = tk.Label(root, font=("Arial", 40), padx=20, pady=10)
clock.pack()

# Alarm Input
tk.Label(root, text="Set Alarm (HH:MM:SS)", font=("Arial", 12)).pack()

alarm_entry = tk.Entry(root, font=("Arial", 14))
alarm_entry.pack(pady=5)

alarm_time = ""

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    status_label.config(text=f"Alarm set for {alarm_time}")

def update_clock():
    current_time = strftime("%H:%M:%S")
    clock.config(text=current_time)

    if alarm_time and current_time == alarm_time:
        messagebox.showinfo("Alarm", "⏰ Wake Up! Alarm Time Reached!")
        status_label.config(text="Alarm Triggered")

    clock.after(1000, update_clock)

# Alarm Button
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=5)

status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
status_label.pack()

update_clock()
root.mainloop()
