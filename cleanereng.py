import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from send2trash import send2trash
import ctypes

def is_hidden_or_system(file_path):
    attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
    if attributes == -1:
        return False
    return bool(attributes & 2) or bool(attributes & 4)

def clean_folder():
    try:
        folder = folder_entry.get()
        days = int(days_entry.get())
        ask_confirmation = confirm_var.get()

        if not os.path.isdir(folder):
            messagebox.showerror("Error", "The specified folder is invalid.")
            return

        limit = days * 86400
        now = time.time()
        deleted_count = 0

        for file_name in os.listdir(folder):
            file_path = os.path.abspath(os.path.join(folder, file_name))  # chemin absolu

            # Debug: print file info
            print("Found file:", file_path)

            if is_hidden_or_system(file_path):
                print("Skipped (hidden/system):", file_path)
                continue

            if os.path.isfile(file_path):
                age = now - os.path.getmtime(file_path)
                if age > limit:
                    if ask_confirmation:
                        response = messagebox.askyesno("Confirm", f"Delete {file_name}?")
                        if not response:
                            continue
                    try:
                        send2trash(file_path)
                        print("Sent to recycle bin:", file_path)
                        deleted_count += 1
                    except Exception as e:
                        print("send2trash failed, deleting permanently:", file_path, e)
                        try:
                            os.remove(file_path)
                            print("Deleted permanently:", file_path)
                            deleted_count += 1
                        except Exception as e2:
                            print("Failed to delete permanently:", file_path, e2)

        messagebox.showinfo("Finished", f"{deleted_count} file(s) removed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for days.")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

# GUI
window = tk.Tk()
window.title("Temporary File Cleaner")

tk.Label(window, text="Folder to clean:").grid(row=0, column=0, sticky="w")
folder_entry = tk.Entry(window, width=40)
folder_entry.grid(row=0, column=1)
tk.Button(window, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(window, text="Delete files older than (days):").grid(row=1, column=0, sticky="w")
days_entry = tk.Entry(window, width=10)
days_entry.grid(row=1, column=1, sticky="w")

confirm_var = tk.BooleanVar()
tk.Checkbutton(window, text="Ask confirmation before deletion", variable=confirm_var).grid(row=2, columnspan=3, sticky="w")

tk.Button(window, text="Start Cleaning", command=clean_folder).grid(row=3, columnspan=3, pady=10)

window.mainloop()
