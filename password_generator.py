import tkinter as tk
import random
import string

def generate():
    try:
        n = int(length.get())
        if n < 4:
            raise ValueError
    except:
        result.delete(0, tk.END)
        result.insert(0, "Length must be 4+")
        return

    chars = ""

    if upper.get():
        chars += string.ascii_uppercase
    if lower.get():
        chars += string.ascii_lowercase
    if numbers.get():
        chars += string.digits
    if symbols.get():
        chars += string.punctuation

    if not chars:
        result.delete(0, tk.END)
        result.insert(0, "Select character type")
        return

    p = ''.join(random.choice(chars) for _ in range(n))
    result.delete(0, tk.END)
    result.insert(0, p)

    score = sum([upper.get(), lower.get(), numbers.get(), symbols.get()])

    if score == 1:
        status.config(text="Strength: Weak")
    elif score == 2:
        status.config(text="Strength: Medium")
    else:
        status.config(text="Strength: Strong")

def copy():
    window.clipboard_clear()
    window.clipboard_append(result.get())
    status.config(text="Password Copied!")

def clear():
    result.delete(0, tk.END)
    status.config(text="Strength: ---")

window = tk.Tk()
window.title("Password Generator")
window.geometry("520x500")
window.minsize(450, 450)

tk.Label(
    window,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(window, text="Password Length",
         font=("Arial", 12, "bold")).pack()

length = tk.Entry(window, width=15,
                  font=("Arial", 13), justify="center")
length.insert(0, "12")
length.pack(pady=5)

tk.Label(window, text="Select Characters",
         font=("Arial", 12, "bold")).pack(pady=12)

upper = tk.BooleanVar(value=True)
lower = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)

f = tk.Frame(window)
f.pack()

tk.Checkbutton(f, text="A-Z", variable=upper).grid(row=0, column=0, padx=8)
tk.Checkbutton(f, text="a-z", variable=lower).grid(row=0, column=1, padx=8)
tk.Checkbutton(f, text="0-9", variable=numbers).grid(row=0, column=2, padx=8)
tk.Checkbutton(f, text="Symbols", variable=symbols).grid(row=0, column=3, padx=8)

tk.Button(
    window,
    text="GENERATE PASSWORD",
    font=("Arial", 12, "bold"),
    command=generate
).pack(pady=18)

result = tk.Entry(
    window,
    width=40,
    font=("Arial", 14),
    justify="center"
)
result.pack(ipady=8)

status = tk.Label(
    window,
    text="Strength: ---",
    font=("Arial", 11, "bold")
)
status.pack(pady=10)

buttons = tk.Frame(window)
buttons.pack(pady=10)

tk.Button(buttons, text="📋 Copy",
          width=12, command=copy).grid(row=0, column=0, padx=5)

tk.Button(buttons, text="🗑 Clear",
          width=12, command=clear).grid(row=0, column=1, padx=5)

window.mainloop()