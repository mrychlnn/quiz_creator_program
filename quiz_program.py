import tkinter as tk
from tkinter import ttk, messagebox

def open_add_question_window():
    add_window = tk.Toplevel(root)
    add_window.title("Quizyowww")
    add_window.geometry("600x700")
    add_window.configure(bg="#f0f4f7")

    tk.Label(add_window, text="Choose category (Math, English, Science, Filipino)").pack(pady=5)
    category_var =tk.StringVar()
    ttk.Combobox(add_window, textvariable=category_var, values=["Math", "English", "Science", "Filipino"]).pack(pady=5)

    tk.Label(add_window, text="Enter the question:").pack()
    question_text = tk.Text(add_window, height=4, width=70)
    question_text.pack()

    tk.Label(add_window, text="Choice a:").pack()
    entry_choice_a = tk.Entry(add_window, width=70)
    entry_choice_a.pack()

    tk.Label(add_window, text="Choice b:").pack()
    entry_choice_b = tk.Entry(add_window, width=70)
    entry_choice_b.pack()

    tk.Label(add_window, text="Choice c:").pack()
    entry_choice_c = tk.Entry(add_window, width=70)
    entry_choice_c.pack()

    tk.Label(add_window, text="Choice d:").pack()
    entry_choice_d = tk.Entry(add_window, width=70)
    entry_choice_d.pack()

    tk.Label(add_window, text="Correct Answer (a, b , c, d):").pack()
    correct_answer_var =tk.StringVar()
    tk.Entry(add_window, textvariable=correct_answer_var, width=10).pack(pady=5)

root = tk.Tk()
root.title("Quizyowww Menu")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

tk.Label(root, text="Quizyowww", font=("Helvetica", 14, "bold"), bg="#e3f2fd").pack(pady=20)

tk.Button(root, text="1. Enter questions", command=open_add_question_window, bg="#4caf50", fg ="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="2. Take a Quiz", bg="#2196f3", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="3. Exit the program", command=root.destroy, bg="#f44336", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)

root.mainloop()