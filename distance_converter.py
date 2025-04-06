import tkinter as tk
from tkinter import ttk
from termcolor import colored


class distance_converter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Distance Converter")

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        frame = feet_to_meter(container)
        frame.grid(row=0, column=0, sticky="NSEW")


        self.bind("<Return>", frame.calculate)
class meters_to_feet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()


        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 10))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable= self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command= self.calculate)

        meters_label.grid(row=0, column=0, sticky="W")
        meters_input.grid(row=0, column=1, sticky="EW")
        meters_input.focus()

        feet_label.grid(row=1, column=0, sticky="W")
        feet_display.grid(row=1, column=1, sticky="EW")
        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"value is {feet:.2f}")
            print(colored(f"{meters} meters is equal to {feet:.2f} feet.", 'white', 'on_green'))
        except ValueError:
            self.feet_value.set("Invalid input")
            print(colored("Empty Value.... Please enter the value", 'white', 'on_red'))

            pass

class feet_to_meter(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 10))
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)

        # Corrected grid layout
        feet_label.grid(row=0, column=0, sticky="W")
        feet_input.grid(row=0, column=1, sticky="EW")
        feet_input.focus()

        meters_label.grid(row=1, column=0, sticky="W")
        meters_display.grid(row=1, column=1, sticky="EW")
        
        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())  # Changed from meters_value to feet_value
            meters = feet / 3.28084
            self.meters_value.set(f"{meters:.2f}")  # Changed from feet_value to meters_value
            print(colored(f"{feet} feet is equal to {meters:.2f} meters.", 'white', 'on_green'))
        except ValueError:
            self.meters_value.set("Invalid input")
            print(colored("Empty Value.... Please enter the value", 'white', 'on_red'))

root = distance_converter()
root.resizable(False, False)

def on_closing(*args):
    print(colored("Closing Window", 'white', 'on_red'))
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.columnconfigure(0, weight=1)

root.mainloop()
