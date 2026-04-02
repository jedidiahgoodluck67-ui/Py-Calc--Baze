import customtkinter as ctk #

# Set the modern look and feel
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Calculator")
        self.geometry("340x550")
        self.resizable(False, False)
        self.configure(fg_color="#1C1C1C") # Dark background from reference

        # --- Logic Variables ---
        self.A = "0"
        self.operator = None
        self.start_new_number = False

        # --- Color Palette (Based on your image) ---
        self.color_bg = "#1C1C1C"
        self.color_num = "#333333"      # Dark gray for numbers
        self.color_func = "#404040"     # Mid gray for top functions
        self.color_accent = "#59C5FF"   # Bright blue from reference
        self.color_text = "white"

        # --- UI Layout ---
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        # Display Label
        self.label = ctk.CTkLabel(
            self, text="0", font=("Arial", 55, "bold"), 
            anchor="e", fg_color="transparent", text_color="white"
        )
        self.label.grid(row=0, column=0, columnspan=4, padx=20, pady=(50, 20), sticky="nsew")

        # Button Grid (All the buttons on the calculator)
        self.button_values = [
            ["AC", "√", "%", "⌫"], 
            ["7", "8", "9", "÷"], 
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["+/-", "0", ".", "+"],
            ["="]
        ]

        self.create_buttons()

    def create_buttons(self):
        for r, row in enumerate(self.button_values):
            for c, value in enumerate(row):
                # Default Styling
                btn_color = self.color_num
                hover_c = "#4D4D4D"
                txt_color = "white"

                # Apply Reference Colors
                if value in ["÷", "×", "-", "+", "=", "⌫"]:
                    btn_color = self.color_accent
                    hover_c = "#80D4FF"
                    txt_color = "black" if value == "=" else "white"
                elif value in ["AC", "√", "%", "+/-"]:
                    btn_color = self.color_func

                # Create the button
                button = ctk.CTkButton(
                    self, text=value, corner_radius=4, border_width=1,
                    border_color="#2B2B2B", fg_color=btn_color,
                    hover_color=hover_c, text_color=txt_color,
                    font=("Arial", 20, "bold"),
                    command=lambda v=value: self.button_clicked(v)
                )
                
                # Grid placement
                if value == "=":
                    button.grid(row=r+1, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")
                else:
                    button.grid(row=r+1, column=c, padx=2, pady=2, sticky="nsew")

    # --- Math & Error Handling Logic (From your snippet) ---
    def divide(self, a, b):
        try:
            result = a / b
            return self.remove_zero_decimal(result)
        except ZeroDivisionError:
            return "Math Error"

    #function to remove unnecesary decimal places
    def remove_zero_decimal(self, num):
        if isinstance(num, str): return num
        if num % 1 == 0:
            return str(int(num))
        return str(round(num, 8))

    def button_clicked(self, value):
        current_text = self.label.cget("text")

        # 1. Back/Delete logic
        if value == "⌫":
            if len(current_text) > 1 and current_text not in ["Math Error", "Input Error"]: #if the text is longer than 1 character and not an error message, delete the last character
                self.label.configure(text=current_text[:-1])
            else:
                self.label.configure(text="0")
            return

        # 2. Operator / Equals Logic
        if value in ["÷", "×", "-", "+", "="]:
            if value == "=":
                if self.operator and self.A is not None:
                    try:
                        numA = float(self.A)
                        numB = float(current_text)
                        
                        if self.operator == "+":
                            res = self.remove_zero_decimal(numA + numB)
                        elif self.operator == "-":
                            res = self.remove_zero_decimal(numA - numB)
                        elif self.operator == "×":
                            res = self.remove_zero_decimal(numA * numB)
                        elif self.operator == "÷":
                            res = self.divide(numA, numB) # Uses your error handling
                        
                        self.label.configure(text=res)
                    except ValueError:
                        self.label.configure(text="Input Error")
                    
                    self.operator = None
                    self.start_new_number = True
            else:
                self.operator = value
                self.A = current_text
                self.start_new_number = True

        # 3. Special Function Buttons
        elif value == "AC":
            self.label.configure(text="0")
            self.A = "0"
            self.operator = None
        elif value == "+/-":
            try:
                self.label.configure(text=self.remove_zero_decimal(float(current_text) * -1))
            except: pass
        elif value == "%":
            try:
                self.label.configure(text=self.remove_zero_decimal(float(current_text) / 100))
            except: pass
        elif value == "√":
            try:
                res = float(current_text) ** 0.5
                self.label.configure(text=self.remove_zero_decimal(res))
                self.start_new_number = True
            except: self.label.configure(text="Input Error")

        # 4. Digits and Decimal logic
        else:
            if self.start_new_number or current_text in ["Math Error", "Input Error"]:
                self.label.configure(text="")
                self.start_new_number = False
                current_text = ""

            if value == ".":
                if "." not in current_text:
                    self.label.configure(text=(current_text if current_text else "0") + ".")
            else:
                if current_text == "0":
                    self.label.configure(text=value)
                else:
                    self.label.configure(text=current_text + value)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()