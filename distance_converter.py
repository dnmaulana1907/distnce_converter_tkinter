import tkinter as tk
from tkinter import ttk
from termcolor import colored

root = tk.Tk()

root.title("Distance Converter")
root.resizable(False, False)

meters_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")

def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(f"value is {feet:.2f}")
        print(colored(f"{meters} meters is equal to {feet:.2f} feet.", 'white', 'on_yellow'))
    except ValueError:
        feet_value.set("Invalid input")
        print(colored("Empty Value.... Please enter the value", 'white', 'on_red'))

        pass

def on_closing(*args):
    print(colored("Closing Window", 'white', 'on_red'))
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
# stay in middle of screen
root.columnconfigure(0, weight=1)


main = ttk.Frame(root, padding=(30, 15))
main.grid()


meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value, font=("Segoe UI", 10))

feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable= feet_value)

calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)


meters_label.grid(row=0, column=0, sticky="W")
meters_input.grid(row=0, column=1, sticky="EW")
meters_input.focus()

feet_label.grid(row=1, column=0, sticky="W")
feet_display.grid(row=1, column=1, sticky="EW")
calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.bind("<Return>", calculate_feet)
root.mainloop()
