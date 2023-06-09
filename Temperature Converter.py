import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Temperature Converter")

def temp_converter(a,b):
    # function takes argument (a)temperature and (b)unit
    b = b.capitalize()
    if b == "Celcius" or b == "C":
        new_temp = (a * 9/5) + 32
        return new_temp
    elif b == "Fahrenheit" or b == "F":
        new_temp = (a - 32) * 5/9
        return new_temp
    else:
        final_label.config(text=f"Result: Invalid Unit.")

def update_temp():
    a = temp_entry.get()
    a = int(a)
    b = unit_entry.get()
    b = b.capitalize()
    if b == "Celcius" or "C":
        new_temp = temp_converter(a,b)
        final_label.config(text=f"Result: {a}{b} = {new_temp}F°")
    elif b == "Fahrenheit" or b == "F":
        new_temp = temp_converter(a,b)
        final_label.config(text=f"Result: {a}{b} = {new_temp}C°")
    else:
        final_label.config(text=f"Result: Invalid Unit.")


temp_label = tk.Label(root, text="Temperature")
temp_label.pack()

temp_entry = tk.Entry(root, )
temp_entry.pack()

unit_label = tk.Label(root, text="Unit")
unit_label.pack()

unit_entry = tk.Entry(root, )
unit_entry.pack()

temp_button = tk.Button(root, text="Convert", command=update_temp)
temp_button.pack()

final_label = tk.Label(root, text=f"Result: ")
final_label.pack()

root.mainloop()