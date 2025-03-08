import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import sympify, symbols, pi

# Function to plot the graph
def plot_graph():
    formula = entry.get()

    # Check if the input is empty
    if not formula:
        messagebox.showerror("Input Error", "Please enter a valid mathematical formula.")
        return
    
    # Try to safely parse the formula
    try:
        # Define the symbol 'x' for sympy
        x = symbols('x')
        
        # Convert the string formula to a sympy expression
        parsed_formula = sympify(formula)
        
        # Generate a range for x (e.g., from -2π to 2π)
        x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        
        # Evaluate the formula for each value of x
        y_vals = np.array([float(parsed_formula.evalf(subs={x: val})) for val in x_vals])

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=formula, color='b')

        # Add labels and grid
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Trigonometric Function Plot")
        ax.grid(True)
        ax.legend()

        # Embed the plot into the Tkinter window
        for widget in frame.winfo_children():
            widget.destroy()  # Clear previous plots

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid formula: {e}")

# Create the main window
root = tk.Tk()
root.title("Interactive Graphing Tool")

# Create the input label and entry field
label = tk.Label(root, text="Enter a trigonometric formula (e.g., 2*sin(3*x + pi/4)):")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create a button to plot the graph
plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack(pady=10)

# Create a frame to hold the graph
frame = tk.Frame(root)
frame.pack()

# Run the Tkinter event loop
root.mainloop()
