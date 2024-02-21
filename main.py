import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_clicked():
    length = length_slider.get()
    password = generate_password(length)
    result_label.config(text=password)

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("สร้างรหัสผ่าน")
root.geometry("300x150")

# สร้างสไลด์เดอร์สำหรับเลือกความยาวของรหัสผ่าน
length_slider = ttk.Scale(root, from_=8, to=100, length=200, orient="horizontal")
length_slider.set(8)
length_slider.pack(pady=10)

# ปุ่มสำหรับสร้างรหัสผ่าน
generate_button = ttk.Button(root, text="สร้างรหัสผ่าน", command=generate_clicked)
generate_button.pack()

# สร้างป้ายกำกับสำหรับแสดงรหัสผ่านที่สร้าง
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
