import tkinter as tk
from tkinter import ttk, messagebox

def open_add_question_window():
    add_window = tk.Toplevel(root)
    add_window.title("Quizyowww")
    add_window.geometry("600x700")
    add_window.configure(bg="#f0f4f7")

    def save_question():
        category = category_var.get().lower()
        if category not in ["math", "english", "science", "filipino"]:
            messagebox.showinfo("Error", "Choose a valid category.")
            return
        
        question = question_text.get("1.0", tk. END).strip()
        choice_a = entry_choice_a.get().strip()
        choice_b = entry_choice_b.get().strip()
        choice_c = entry_choice_c.get().strip()
        choice_d = entry_choice_d.get().strip()
        correct_answer = correct_answer_var.get().strip().lower()

        if not all([question, choice_a, choice_b, choice_c, choice_d]) or correct_answer not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Please fill the fields and choose a valid correct answer (a-d).")
            return
        
        file_name = f"{category}.txt"
        saving_file = open(file_name, "a")
        saving_file.write(f"Question: {question}\n")
        saving_file.write(f"a) {choice_a}\n")
        saving_file.write(f"b) {choice_b}\n")
        saving_file.write(f"c) {choice_c}\n")
        saving_file.write(f"d) {choice_d}\n")
        saving_file.write(f"Correct answer: {correct_answer}\n")
        saving_file.write("-----\n")
        saving_file.close()

        messagebox.showinfo("Saved", f"Question saved to {file_name}")
        clear_fields()

    def clear_fields():
        question_text.delete("1.0", tk.END)
        entry_choice_a.delete(0, tk.END)
        entry_choice_b.delete(0, tk.END)
        entry_choice_c.delete(0, tk.END)
        entry_choice_d.delete(0, tk.END)
        correct_answer_var.set("")

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

    tk.Button(add_window, text="Save Question", command=save_question, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

root = tk.Tk()
root.title("Quizyowww Menu")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

tk.Label(root, text="Quizyowww", font=("Helvetica", 14, "bold"), bg="#e3f2fd").pack(pady=20)

tk.Button(root, text="1. Enter questions", command=open_add_question_window, bg="#4caf50", fg ="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="2. Take a Quiz", bg="#2196f3", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)
tk.Button(root, text="3. Exit the program", command=root.destroy, bg="#f44336", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)

root.mainloop()