import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Quizyowww Menu")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

tk.Label(root, text="Quizyowww", font=("Helvetica", 14, "bold"), bg="#e3f2fd").pack(pady=20)

tk.Button(root, text="1. Enter questions", bg="#4caf50", fg ="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="2. Take a Quiz", bg="#2196f3", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="3. Exit the program", command=root.destroy, bg="#f44336", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)

root.mainloop()