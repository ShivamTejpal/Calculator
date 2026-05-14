import tkinter

# ---------------- COLORS ----------------
COLOR_BLACK = "#000000"
COLOR_DARK_GRAY = "#333333"
COLOR_LIGHT_GRAY = "#A5A5A5"
COLOR_ORANGE = "#FF9F0A"
COLOR_WHITE = "#FFFFFF"

# ---------------- BUTTON VALUES ----------------
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# ---------------- STATE ----------------
current_input = ""
previous_input = ""
operator = ""
result_shown = False

# ---------------- WINDOW ----------------
window = tkinter.Tk()
window.title("Calculator")
window.configure(bg=COLOR_BLACK)
window.resizable(False, False)
window.geometry("430x700")

# ---------------- FRAME ----------------
frame = tkinter.Frame(window, bg=COLOR_BLACK, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# ---------------- DISPLAY ----------------
small_label = tkinter.Label(
    frame,
    text="",
    bg=COLOR_BLACK,
    fg="#888888",
    font=("Helvetica", 18),
    anchor="e"
)
small_label.grid(row=0, column=0, columnspan=4, sticky="we", pady=(15, 0))

label = tkinter.Label(
    frame,
    text="0",
    bg=COLOR_BLACK,
    fg=COLOR_WHITE,
    font=("Helvetica", 58),
    anchor="e",
    padx=15,
    pady=20
)
label.grid(row=1, column=0, columnspan=4, sticky="we", pady=(0, 20))

# ---------------- LOGIC ----------------
def update_display(value, small=""):
    # Shrink font if text is long
    length = len(str(value))
    if length > 9:
        label.config(font=("Helvetica", 36))
    elif length > 6:
        label.config(font=("Helvetica", 48))
    else:
        label.config(font=("Helvetica", 58))
    label.config(text=value)
    small_label.config(text=small)

def button_clicked(value):
    global current_input, previous_input, operator, result_shown

    if value == "AC":
        current_input = ""
        previous_input = ""
        operator = ""
        result_shown = False
        update_display("0")

    elif value == "+/-":
        if current_input and current_input != "0":
            if current_input.startswith("-"):
                current_input = current_input[1:]
            else:
                current_input = "-" + current_input
            update_display(current_input)

    elif value == "%":
        if current_input:
            try:
                current_input = str(float(current_input) / 100)
                # Clean up unnecessary decimals
                if current_input.endswith(".0"):
                    current_input = current_input[:-2]
                update_display(current_input)
            except ValueError:
                pass

    elif value == "√":
        if current_input:
            try:
                num = float(current_input)
                if num < 0:
                    update_display("Error")
                    current_input = ""
                else:
                    result = num ** 0.5
                    current_input = str(int(result) if result == int(result) else round(result, 10))
                    update_display(current_input)
            except ValueError:
                pass

    elif value in ["÷", "×", "-", "+"]:
        if current_input:
            previous_input = current_input
            operator = value
            small_label.config(text=f"{previous_input} {operator}")
            current_input = ""
            result_shown = False
        elif previous_input:
            # Allow changing operator
            operator = value
            small_label.config(text=f"{previous_input} {operator}")

    elif value == "=":
        if previous_input and current_input and operator:
            try:
                a = float(previous_input)
                b = float(current_input)
                small_label.config(text=f"{previous_input} {operator} {current_input} =")
                if operator == "÷":
                    if b == 0:
                        update_display("Error", small_label.cget("text"))
                        current_input = ""
                        previous_input = ""
                        operator = ""
                        return
                    result = a / b
                elif operator == "×":
                    result = a * b
                elif operator == "-":
                    result = a - b
                elif operator == "+":
                    result = a + b
                # Clean up result display
                if result == int(result):
                    current_input = str(int(result))
                else:
                    current_input = str(round(result, 10))
                update_display(current_input, small_label.cget("text"))
                previous_input = ""
                operator = ""
                result_shown = True
            except Exception:
                update_display("Error")
                current_input = ""

    elif value == ".":
        if result_shown:
            current_input = "0"
            result_shown = False
        if "." not in current_input:
            current_input = (current_input or "0") + "."
            update_display(current_input)

    else:  # digit
        if result_shown:
            current_input = ""
            result_shown = False
        if current_input == "0":
            current_input = value
        else:
            current_input += value
        update_display(current_input)

# ---------------- MACOS-COMPATIBLE BUTTON (Label-based) ----------------
def make_button(parent, text, bg, fg, row, column, columnspan=1, anchor="center", padx_inner=0):
    """
    Uses a Label instead of Button to ensure bg/fg colors render correctly on macOS.
    Hover and click effects are handled via bind().
    """
    # Determine hover/press colors
    if bg == COLOR_ORANGE:
        hover_bg = "#E08800"
        press_bg = "#C07700"
    elif bg == COLOR_LIGHT_GRAY:
        hover_bg = "#C0C0C0"
        press_bg = "#909090"
    else:
        hover_bg = "#555555"
        press_bg = "#222222"

    lbl = tkinter.Label(
        parent,
        text=text,
        bg=bg,
        fg=fg,
        font=("Helvetica", 30),
        anchor=anchor,
        padx=padx_inner if padx_inner else 0,
        cursor="hand2"
    )
    lbl.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        padx=6,
        pady=6,
        sticky="nsew"
    )

    # Rounded-feel via events
    lbl.bind("<Enter>",        lambda e: lbl.config(bg=hover_bg))
    lbl.bind("<Leave>",        lambda e: lbl.config(bg=bg))
    lbl.bind("<ButtonPress-1>",   lambda e: lbl.config(bg=press_bg))
    lbl.bind("<ButtonRelease-1>", lambda e: (lbl.config(bg=hover_bg), button_clicked(text)))

    return lbl

# ---------------- BUILD BUTTONS ----------------
for row_idx in range(len(button_values)):
    for col_idx in range(len(button_values[row_idx])):
        value = button_values[row_idx][col_idx]

        if value in top_symbols:
            bg_color, fg_color = COLOR_LIGHT_GRAY, COLOR_BLACK
        elif value in right_symbols:
            bg_color, fg_color = COLOR_ORANGE, COLOR_WHITE
        else:
            bg_color, fg_color = COLOR_DARK_GRAY, COLOR_WHITE

        grid_row = row_idx + 2

        if value == "0":
            make_button(frame, value, bg_color, fg_color,
                        row=grid_row, column=0, columnspan=2,
                        anchor="w", padx_inner=30)
        else:
            real_col = col_idx
            if row_idx == 4 and col_idx > 0:
                real_col += 1
            make_button(frame, value, bg_color, fg_color,
                        row=grid_row, column=real_col, columnspan=1)

# ---------------- GRID CONFIG ----------------
for i in range(7):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

# ---------------- RUN ----------------
window.mainloop()