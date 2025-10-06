import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill="both", ipadx=8, pady=10)

# Button click function
def click(value):
    if value == "=":
        try:
            # Evaluate the expression in the entry box
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Add buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for b in row:
        tk.Button(frame, text=b, font=("Arial", 18), command=lambda x=b: click(x), height=2, width=5).pack(side="left", expand=True, fill="both")

# Run the GUI
root.mainloop()
