start_new_number = False
def remove_zero_decimal(number):
    """Helper to show 5 instead of 5.0"""
    try:
        # Convert to float first to handle strings or numbers
        n = float(number)
        if n.is_integer():
            return str(int(n))
        return str(n)
    except:
        return str(number)

def button_clicked(value, label, history_label):
    global A, operator, start_new_number
def button_clicked(value, label, history_label):
    global A, operator, start_new_number

    current_text = label.cget("text")

    # 1. Handling Calculation (=)
    if value == "=":
        if A is not None and operator is not None:
            numA = float(A)
            numB = float(current_text)

            if operator == "+": res = numA + numB
            elif operator == "-": res = numA - numB
            elif operator == "×": res = numA * numB
            elif operator == "÷": res = numA / numB if numB != 0 else "Error"
            
            label.configure(text=remove_zero_decimal(res))
            history_label.configure(text="") # Clear history after result
            A = "0"
            operator = None
            start_new_number = True 

    # 2. Handling Operators (+, -, ×, ÷)
    elif value in ["+", "-", "×", "÷"]:
        operator = value
        A = current_text
        start_new_number = True
        # Fixed the 'test' to 'text' here
        history_label.configure(text=f"{A} {operator}")

    # 3. Handling Special Functions (C, +/-, etc.)
    elif value == "C":
        label.configure(text="0")
        history_label.configure(text="")
        A = "0"
        operator = None
    elif value == "+/-":
        label.configure(text=remove_zero_decimal(float(current_text) * -1))
    
    # 4. Handling Digits and Decimals
    else:
        if start_new_number:
            display_val = ""
            start_new_number = False
        else:
            display_val = current_text

        if value == ".":
            if "." not in display_val:
                label.configure(text=display_val + value)
        else:
            if display_val == "0":
                label.configure(text=value)
            else:
                label.configure(text=display_val + value)