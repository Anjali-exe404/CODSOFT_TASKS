import tkinter as tk

def click(value):
    if entry.get() == "Error":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")
window.geometry("360x500")
window.resizable(True, True)

entry = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)
entry.pack(fill="x", padx=10, pady=15, ipady=10)

frame = tk.Frame(window)
frame.pack(expand=True, fill="both", padx=10)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("=", 3, 3)
]

for text, row, col in buttons:
    if text == "=":
        command = calculate
    else:
        command = lambda x=text: click(x)

    tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        command=command
    ).grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=3,
        pady=3
    )

for i in range(4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 16),
    command=clear
).pack(fill="x", padx=13, pady=10)

window.mainloop()