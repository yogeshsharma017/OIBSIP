import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import os

DATA_FILE = "bmi_data.txt"

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")
        bmi = weight / (height / 100) ** 2
        categories = {
            (0, 18.5): "Underweight",
            (18.5, 24.9): "Normal weight",
            (25, 29.9): "Overweight",
            (30, float('inf')): "Obese"
        }
        bmi_category = None
        for range_, category in categories.items():
            if range_[0] <= bmi < range_[1]:
                bmi_category = category
                break
        label_result.config(text=f"BMI Value: {bmi:.2f}\nCategory: {bmi_category}", foreground="black")
        with open(DATA_FILE, 'a') as file:
            file.write(f"{bmi}\n")
        return bmi
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
        return None
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def visualize_bmi_history():
    try:
        with open(DATA_FILE, 'r') as file:
            bmi_history = [float(line.strip()) for line in file.readlines()]
            if len(bmi_history) < 2:
                raise ValueError("At least two BMI values are required to visualize history.")
            plt.plot(bmi_history, marker='o', color='black')
            plt.xlabel('Measurements', color='black')
            plt.ylabel('BMI', color='black')
            plt.title('Historical BMI Data', color='black')
            plt.grid(True)
            plt.show()
    except FileNotFoundError:
        messagebox.showinfo("No Data", "No historical BMI data found.")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("BMIMeter by Yogesh Sharma")
app.geometry("400x300")
app.configure(bg="white")

style = ttk.Style()
style.theme_use("clam")
style.configure('.', background='white', foreground='black', font=('Helvetica', 10))
style.map('.', background=[('pressed', '!disabled', 'gray')])

label_height = ttk.Label(app, text="Height (in cm):")
label_height.pack(pady=5)
entry_height = ttk.Entry(app)
entry_height.pack(pady=5)

label_weight = ttk.Label(app, text="Weight (in kg):")
label_weight.pack(pady=5)
entry_weight = ttk.Entry(app)
entry_weight.pack(pady=5)

button_calculate = ttk.Button(app, text="Calculate", command=calculate_bmi, style='Modern.TButton')
style.configure('Modern.TButton', background='black', foreground='white', borderwidth=0, relief='flat')
style.map('Modern.TButton', background=[('active', 'gray')])
button_calculate.pack(pady=10)

label_result = ttk.Label(app, text="BMI: ")
label_result.pack(pady=10)

button_visualize = ttk.Button(app, text="Visualize BMI History", command=visualize_bmi_history, style='Modern.TButton')
button_visualize.pack(pady=10)

app.mainloop()
