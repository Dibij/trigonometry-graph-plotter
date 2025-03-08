# Interactive Graphing Tool

This is a simple Python-based graphical user interface (GUI) application that allows users to input a trigonometric formula and visualize its graph. The tool uses **Tkinter** for the GUI and **Matplotlib** for plotting the graph, alongside **SymPy** for symbolic mathematical calculations.

## Features

- Input a trigonometric formula (e.g., `2*sin(3*x + pi/4)`).
- Plot the graph of the formula for values of x in the range from `-2π` to `2π`.
- Real-time error handling for invalid input.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Matplotlib
- Numpy
- SymPy

You can install the required libraries with pip:

```bash
pip install matplotlib numpy sympy
```

## How to Use

1. Clone or download the repository to your local machine.
2. Open the file in your preferred IDE or text editor (e.g., VSCode).
3. Run the Python script.
4. The GUI will open with a text input box where you can enter any valid trigonometric formula. For example:
   - `2*sin(3*x + pi/4)`
   - `sin(x) + cos(x)`
5. Click the "Plot Graph" button to visualize the graph of your formula.
6. If you enter an invalid formula, an error message will appear.

## Example

For the input `2*sin(3*x + pi/4)`, the graph of the function will be plotted in the window, showing the behavior of the trigonometric expression across the defined range of x values.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
