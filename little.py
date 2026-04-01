import tkinter as tk
import customtkinter as ctk

# Set themes
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Baze Group G Modern Calc")
root.geometry("1980x800")

# Logic Functions
def add_to_expression(value):
    current_text = main_entry.get()
    main_entry.delete(0, tk.END)
    main_entry.insert(0, current_text + str(value))

def calculate():
    try:
        result = eval(main_entry.get())
        result_display_label.configure(text=f"Result: {result}", text_color="#2ecc71")
    except Exception:
        result_display_label.configure(text="Error: Invalid Input", text_color="#e74c3c")

def clear_entry():
    main_entry.delete(0, tk.END)
    result_display_label.configure(text="Result: --", text_color="#2ecc71")

# --- UI Layout ---

# 1. Main Display Entry (Infinite numbers go here)
label1 = ctk.CTkLabel(root, text="Enter Expression:", font=("Helvetica", 14))
label1.pack(pady=(20, 0))

main_entry = ctk.CTkEntry(root, placeholder_text="e.g. 5 + 10 * 2 / 3", width=320, height=50, corner_radius=10, font=("Helvetica", 18))
main_entry.pack(pady=10)

# 2. Operations Frame
ops_frame = ctk.CTkFrame(root, fg_color="transparent")
ops_frame.pack(pady=10)

# Buttons for operators
operators = [("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")]

for text, char in operators:
    ctk.CTkButton(ops_frame, text=text, width=60, height=60, corner_radius=30, 
                  command=lambda c=char: add_to_expression(c)).pack(side="left", padx=5)

# 3. Utility Buttons (Clear & Equals)
btn_frame = ctk.CTkFrame(root, fg_color="transparent")
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="Clear", width=100, height=50, fg_color="#95a5a6", 
              hover_color="#7f8c8d", command=clear_entry).pack(side="left", padx=5)

equals_btn = ctk.CTkButton(btn_frame, text="=", width=210, height=50, fg_color="#e67e22", 
                           hover_color="#d35400", font=("Helvetica", 20, "bold"), 
                           command=calculate)
equals_btn.pack(side="left", padx=5)

# 4. Results
result_display_label = ctk.CTkLabel(root, text="Result: --", font=("Helvetica", 24, "bold"), text_color="#2ecc71")
result_display_label.pack(pady=30)

root.mainloop()