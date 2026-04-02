import customtkinter as ctk
from PIL import Image, ImageTk
import ctypes

# Windows Taskbar Logo
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('baze.calc.v1')
except:
    pass

# --- Constants ---
COLOR_BG = "#1A1A1A"          
COLOR_BTN_NUM = "#333333"    
COLOR_BTN_OP = "#2D2D2D"      
COLOR_ACCENT = "#D24A14"  
COLOR_TEXT = "#FFFFFF"

app = ctk.CTk()
app.title("Baze University Calc")
app.geometry("320x550")
app.configure(fg_color=COLOR_BG)

# --- Icon Setup ---
# Used .ico for the windows title bar
try:
    # Set the Window Icon (Title Bar)
    app.iconbitmap("images (2).ico") 
except:
    # Fallback if you only have the PNG
    img = ImageTk.PhotoImage(Image.open("Y2k.png"))
    app.wm_iconphoto(True, img)
# Window logo
icon_image = Image.open("Y2k.png")

icon_photo = ImageTk.PhotoImage(icon_image)

app.wm_iconphoto(True, icon_photo)

try:
    logo_img = ctk.CTkImage(light_image=Image.open("Y2k.png"),
                            dark_image=Image.open("Y2k.png"),
                            size=(20, 20))
except Exception as e:
    print(f"Logo not found, using placeholder. Error: {e}")
    logo_img = None


# --- Basic button layout ---
button_values = [
    ["C", "÷", "×", "⌫"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "+/-", ""]
]
operators = ["÷", "×", "-", "+", "⌫", "C", "+/-"]

# --- UI Containers ---
frame = ctk.CTkFrame(app, fg_color=COLOR_BG)
frame.pack(expand=True, fill="both", padx=10, pady=10)


# 2. Display Label
label = ctk.CTkLabel(
    frame, text="0", font=("Arial", 55), 
    anchor="e", text_color=COLOR_TEXT, height=120
)
label.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=(20, 10))

# Button Generation 
# I Used enumerate to get row/column indices for grid positioning
for row_idx, row_list in enumerate(button_values):
    for col_idx, value in enumerate(row_list):
        if not value: continue 
        
        # Determine Color Logic
        if value == "=":
            fg = COLOR_ACCENT
            hover = "#A03810"
            text_col = "#FFFFFF"
        elif value in operators:
            fg = COLOR_BTN_OP
            hover = "#3D3D3D"
            text_col = COLOR_TEXT
        else:
            fg = COLOR_BTN_NUM
            hover = "#454545"
            text_col = COLOR_TEXT

        btn = ctk.CTkButton(
            frame,
            text=value,
            width=70,
            height=70,
            corner_radius=12,
            fg_color=fg,
            text_color=text_col,
            hover_color=hover,
            font=("Arial", 20, "bold"),
            command=lambda v=value: print(f"Clicked: {v}")
        )
        # Offset by row 1 because the display label is row 0
        btn.grid(row=row_idx + 1, column=col_idx, padx=3, pady=3, sticky="nsew")

# Configure grid weights
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    frame.grid_rowconfigure(i, weight=1) # Weight allows for the buttons to adjust based on the geometry 

app.mainloop()