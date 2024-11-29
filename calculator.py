import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve
from collections import Counter

# Initialize history list and AI suggestion
history = []
ai_suggestions = Counter()

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get()) if entry_num2.get() else None
        result = None

        # Perform operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operation == "Square":
            result = num1 ** 2
        elif operation == "Square Root":
            if num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            result = math.sqrt(num1)
        elif operation == "Factorial":
            if num1 < 0 or not num1.is_integer():
                raise ValueError("Factorial is only defined for non-negative integers.")
            result = math.factorial(int(num1))

        # Display result
        result_label.config(text=f"Result: {result}", fg="#4caf50")

        # Add to history and update AI suggestions
        history.append(f"{operation}: {num1} {' ' + str(num2) if num2 else ''} = {result}")
        ai_suggestions[operation] += 1

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except ZeroDivisionError as zde:
        messagebox.showerror("Error", str(zde))

# Show history window
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.configure(bg="#f7f7f7")

    tk.Label(history_window, text="Calculation History:", font=("Arial", 14, "bold"), bg="#f7f7f7").pack(pady=10)

    if not history:
        tk.Label(history_window, text="No calculations yet.", font=("Arial", 12), bg="#f7f7f7").pack()
    else:
        for calc in history:
            tk.Label(history_window, text=calc, font=("Arial", 12), bg="#f7f7f7").pack()

# AI prediction
def predict_operation():
    if ai_suggestions:
        most_common_operation = ai_suggestions.most_common(1)[0][0]
        messagebox.showinfo("AI Prediction", f"Based on your history, you might want to perform: {most_common_operation}")
    else:
        messagebox.showinfo("AI Prediction", "Not enough data to make a prediction.")

# Solve equation
def solve_equation():
    try:
        x = symbols('x')
        equation = equation_entry.get()
        equation = equation.replace("^", "**")  # Convert ^ to ** for Python
        eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
        solution = solve(eq, x)
        equation_result_label.config(text=f"Solution: x = {solution}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation: {e}")

# Plot graph
def plot_graph():
    try:
        expression = graph_entry.get()
        expression = expression.replace("^", "**")  # Convert ^ to ** for Python
        x = np.linspace(-10, 10, 400)
        y = eval(expression)
        plt.plot(x, y, label=f"y = {expression}")
        plt.title("Graph Plotter")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid function: {e}")

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator with Buttons")
root.geometry("500x700")
root.configure(bg="#f0f8ff")

# Header
header = tk.Label(root, text="Scientific Calculator", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#2f4f4f")
header.grid(row=0, column=0, columnspan=4, pady=10)

# Input fields
tk.Label(root, text="Enter first number:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
entry_num1 = tk.Entry(root, font=("Arial", 12), width=15)
entry_num1.grid(row=1, column=2, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Enter second number (if applicable):", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
entry_num2 = tk.Entry(root, font=("Arial", 12), width=15)
entry_num2.grid(row=2, column=2, columnspan=2, padx=10, pady=5)

# Buttons for operations
button_add = tk.Button(root, text="+", command=lambda: calculate("Add"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_add.grid(row=3, column=0, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", command=lambda: calculate("Subtract"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_subtract.grid(row=3, column=1, padx=5, pady=5)

button_multiply = tk.Button(root, text="x", command=lambda: calculate("Multiply"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_multiply.grid(row=3, column=2, padx=5, pady=5)

button_divide = tk.Button(root, text="÷", command=lambda: calculate("Divide"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_divide.grid(row=3, column=3, padx=5, pady=5)

button_square = tk.Button(root, text="x²", command=lambda: calculate("Square"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_square.grid(row=4, column=0, padx=5, pady=5)

button_sqrt = tk.Button(root, text="√x", command=lambda: calculate("Square Root"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_sqrt.grid(row=4, column=1, padx=5, pady=5)

button_factorial = tk.Button(root, text="n!", command=lambda: calculate("Factorial"), font=("Arial", 12), bg="#4caf50", fg="white", width=5)
button_factorial.grid(row=4, column=2, padx=5, pady=5)

button_history = tk.Button(root, text="History", command=show_history, font=("Arial", 12), bg="#008cba", fg="white", width=10)
button_history.grid(row=5, column=0, columnspan=2, pady=10)

button_ai = tk.Button(root, text="AI Suggestion", command=predict_operation, font=("Arial", 12), bg="#ff9800", fg="white", width=10)
button_ai.grid(row=5, column=2, columnspan=2, pady=10)

# Equation solving
tk.Label(root, text="Enter equation (e.g., x^2 + 2*x + 1 = 0):", font=("Arial", 12), bg="#f0f8ff").grid(row=6, column=0, columnspan=4, padx=10, pady=5, sticky="w")
equation_entry = tk.Entry(root, font=("Arial", 12), width=40)
equation_entry.grid(row=7, column=0, columnspan=4, padx=10, pady=5)
solve_button = tk.Button(root, text="Solve Equation", command=solve_equation, font=("Arial", 12), bg="#ff5722", fg="white", width=15)
solve_button.grid(row=8, column=0, columnspan=4, pady=10)

equation_result_label = tk.Label(root, text="Solution: ", font=("Arial", 12), bg="#f0f8ff", fg="#2f4f4f")
equation_result_label.grid(row=9, column=0, columnspan=4, pady=5)

# Graph plotting
tk.Label(root, text="Enter function for graph (e.g., x^2):", font=("Arial", 12), bg="#f0f8ff").grid(row=10, column=0, columnspan=4, padx=10, pady=5, sticky="w")
graph_entry = tk.Entry(root, font=("Arial", 12), width=40)
graph_entry.grid(row=11, column=0, columnspan=4, padx=10, pady=5)
plot_button = tk.Button(root, text="Plot Graph", command=plot_graph, font=("Arial", 12), bg="#ff69b4", fg="white", width=15)
plot_button.grid(row=12, column=0, columnspan=4, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#2f4f4f")
result_label.grid(row=13, column=0, columnspan=4, pady=10)

# Run the GUI
root.mainloop()
