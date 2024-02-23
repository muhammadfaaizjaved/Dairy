import tkinter as tk
from tkinter import messagebox

def save_entry():
    entry = entry_text.get("1.0", "end-1c")
    if entry:
        with open("diary.txt", "a") as f:
            f.write(entry + "\n")
        messagebox.showinfo("Success", "Entry saved successfully.")
        entry_text.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", "Entry cannot be empty.")

def read_entries():
    try:
        with open("diary.txt", "r") as f:
            diary_content = f.read()
        messagebox.showinfo("Diary Entries", diary_content)
    except FileNotFoundError:
        messagebox.showerror("Error", "No entries found.")

# GUI setup
root = tk.Tk()
root.title("My Daily Diary")

label = tk.Label(root, text="Write your daily entry below:")
label.pack()

entry_text = tk.Text(root, height=10, width=50)
entry_text.pack()

save_button = tk.Button(root, text="Save Entry", command=save_entry)
save_button.pack()

read_button = tk.Button(root, text="Read Entries", command=read_entries)
read_button.pack()

root.mainloop()
