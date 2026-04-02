import customtkinter as ctk
from PIL import Image, ImageTk
import ctypes
from Functions import button_clicked

# Windows taskbar logo
try:
    # This allows for our logo to show up instead of the python snake 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('baze.calc.v1')
except:
    pass

# Stylization Constants
COLOR_BG = "#1A1A1A"          
COLOR_BTN_NUM = "#333333"    
COLOR_BTN_OP = "#2D2D2D"      
COLOR_ACCENT = "#D24A14"  
COLOR_TEXT = "#FFFFFF"

# Window set up 
app = ctk.CTk()
app.title("Baze University Calc")
app.geometry("340x600")
app.configure(fg_color=COLOR_BG)

# Icon and logo setup
try:
    # Window Title Bar Icon
    app.iconbitmap("images (2).ico") 
except:
    try:
        # This makes the image revert to .png if .ico isn't found for whatever reason 
        img = ImageTk.PhotoImage(Image.open("Y2k.png"))
        app.wm_iconphoto(True, img)
    except:
        print("Icon files not found. Skipping icon setup.")

# UI config
frame = ctk.CTkFrame(app, fg_color=COLOR_BG)
frame.pack(expand=True, fill="both", padx=15, pady=15)

# 
history_label = ctk.CTkLabel(
    frame, text="", font=("Arial", 18), 
    anchor="e", text_color="#888888" 
)
history_label.grid(row=0, column=0, columnspan=4, sticky="we", padx=10)

# 2. Main Display Label (The "Result" display)
label = ctk.CTkLabel(
    frame, text="0", font=("Arial", 55), 
    anchor="e", text_color=COLOR_TEXT, height=100
)
label.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=(0, 20))

# --- Button Configuration ---
button_values = [
    ["C", "÷", "×", "⌫"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "+/-", ""]
]
operators = ["÷", "×", "-", "+", "⌫", "C", "+/-"]

# --- Button Generation Loop ---
for row_idx, row_list in enumerate(button_values):
    for col_idx, value in enumerate(row_list):
        if not value: continue 
        
        # Color Logic based on button type
        if value == "=":
            fg, hover = COLOR_ACCENT, "#A03810"
        elif value in operators:
            fg, hover = COLOR_BTN_OP, "#3D3D3D"
        else:
            fg, hover = COLOR_BTN_NUM, "#454545"

        btn = ctk.CTkButton(
            frame,
            text=value,
            width=75, height=75,
            corner_radius=15,
            fg_color=fg,
            hover_color=hover,
            text_color=COLOR_TEXT,
            font=("Arial", 22, "bold"),
            # Passing all 3 required arguments to your function
            command=lambda v=value: button_clicked(v, label, history_label)
        )
        # Offset by 2 rows to account for History (row 0) and Main (row 1)
        btn.grid(row=row_idx + 2, column=col_idx, padx=4, pady=4, sticky="nsew")

# --- Responsive Grid Weights ---
for i in range(4): 
    frame.grid_columnconfigure(i, weight=1)
for i in range(2, 7): 
    frame.grid_rowconfigure(i, weight=1)

if __name__ == "__main__":
    app.mainloop()