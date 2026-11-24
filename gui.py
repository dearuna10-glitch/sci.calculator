
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

# ---------------- COLORS ----------------

BG = "#101827"
PANEL = "#1E293B"
BUTTON = "#334155"
ACCENT = "#38BDF8"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("850x700")
root.configure(bg=BG)
root.resizable(False, False)

# ---------------- HEADER ----------------

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=35, pady=25)

tk.Label(
    header,
    text="∑  SCIENTIFIC CALCULATOR",
    font=("Segoe UI", 23, "bold"),
    bg=BG,
    fg=ACCENT
).pack(anchor="w")

tk.Label(
    header,
    text="ADVANCED MATHEMATICAL COMPUTATION SYSTEM",
    font=("Segoe UI", 9),
    bg=BG,
    fg=MUTED
).pack(anchor="w", pady=5)

# ---------------- MAIN PANEL ----------------

panel = tk.Frame(root, bg=PANEL)
panel.pack(fill="both", expand=True, padx=35, pady=10)

# Operation selector

tk.Label(
    panel,
    text="SELECT OPERATION",
    font=("Segoe UI", 11, "bold"),
    bg=PANEL,
    fg=TEXT
).pack(anchor="w", padx=25, pady=(25, 8))

operations = [
    "1 - Addition",
    "2 - Subtraction",
    "3 - Multiplication",
    "4 - Division",
    "5 - Operation 5",
    "6 - Power",
    "7 - Modulus",
    "8 - Root",
    "9 - Square Root",
    "10 - Factorial",
    "11 - Sine",
    "12 - Cosine",
    "13 - Tangent",
    "14 - Logarithm",
    "15 - Degrees",
    "16 - Radians",
    "17 - Percentage",
    "18 - Pi",
    "19 - Power of 10",
    "20 - Exponential",
    "21 - Inverse Trigonometric",
    "22 - Hyperbolic",
    "23 - Inverse Hyperbolic",
    "24 - Integral",
    "25 - Derivative",
    "26 - Combination",
    "27 - Permutation",
    "28 - Matrix Operations",
    "29 - Complex Number Operations",
    "30 - Solve Equations"
]

operation_box = ttk.Combobox(
    panel,
    values=operations,
    state="readonly",
    font=("Segoe UI", 12)
)
operation_box.pack(fill="x", padx=25, ipady=8)
operation_box.current(0)

# ---------------- NUMBER INPUT ----------------

tk.Label(
    panel,
    text="ENTER NUMBERS",
    font=("Segoe UI", 11, "bold"),
    bg=PANEL,
    fg=TEXT
).pack(anchor="w", padx=25, pady=(25, 8))

number_entry = tk.Entry(
    panel,
    font=("Segoe UI", 15),
    bg="#0F172A",
    fg=TEXT,
    insertbackground=ACCENT,
    relief="flat"
)
number_entry.pack(fill="x", padx=25, ipady=12)

tk.Label(
    panel,
    text="Enter numbers separated by spaces",
    font=("Segoe UI", 9),
    bg=PANEL,
    fg=MUTED
).pack(anchor="w", padx=25, pady=6)

# ---------------- RESULT DISPLAY ----------------

tk.Label(
    panel,
    text="CALCULATION RESULT",
    font=("Segoe UI", 11, "bold"),
    bg=PANEL,
    fg=TEXT
).pack(anchor="w", padx=25, pady=(25, 8))

result_box = tk.Text(
    panel,
    height=5,
    font=("Consolas", 14),
    bg="#0F172A",
    fg=ACCENT,
    relief="flat",
    wrap="word"
)
result_box.pack(fill="x", padx=25)

# ---------------- CALCULATE ----------------

def calculate():

    selected = operation_box.get()

    if not selected:
        messagebox.showwarning("Warning", "Select an operation.")
        return

    numbers = number_entry.get().strip()

    if not numbers:
        messagebox.showwarning("Warning", "Enter your numbers.")
        return

    choice = selected.split(" - ")[0]

    backend_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "backend.py"
    )

    try:

        # Send the existing backend its inputs
        user_input = numbers + "\n" + choice + "\n"

        process = subprocess.run(
            [sys.executable, backend_path],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=15
        )

        output = process.stdout.strip()
        errors = process.stderr.strip()

        result_box.delete("1.0", tk.END)

        if process.returncode != 0:
            result_box.insert(
                tk.END,
                "Backend error:\n" + errors
            )
        elif "Result:" in output:
            result_box.insert(
                tk.END,
                output[output.rfind("Result:"):]
            )
        else:
            result_box.insert(tk.END, output)

    except Exception as error:
        messagebox.showerror("Error", str(error))


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(panel, bg=PANEL)
button_frame.pack(pady=25)

calculate_btn = tk.Button(
    button_frame,
    text="CALCULATE  →",
    font=("Segoe UI", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    activebackground="#7DD3FC",
    relief="flat",
    cursor="hand2",
    command=calculate,
    padx=35,
    pady=13
)
calculate_btn.pack(side="left", padx=10)


def clear():
    number_entry.delete(0, tk.END)
    result_box.delete("1.0", tk.END)
    operation_box.current(0)

clear_btn = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Segoe UI", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground="#475569",
    relief="flat",
    cursor="hand2",
    command=clear,
    padx=35,
    pady=13
)
clear_btn.pack(side="left", padx=10)

# ---------------- FOOTER ----------------

tk.Label(
    root,
    text="SCIENTIFIC COMPUTING  •  PYTHON POWERED",
    font=("Segoe UI", 9),
    bg=BG,
    fg=MUTED
).pack(pady=12)

root.mainloop()
