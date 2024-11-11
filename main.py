import tkinter as tk
from scipy.optimize import linprog
from tkinter import messagebox

def solve_truck_problem(rhs1, rhs2, rhs3, rhs4):
    # Coefficients of the objective function (minimize x + y)
    c = [1, 1, 1, 1]  # Coefficients for x and y

    # Coefficients for the constraints (LHS of inequalities)
    A = [
        [-75, -15, -15, -15],
        [-15, -75, -15, -15],
        [-15, -15, -75, -15],
        [-15, -15, -15, -75]
    ]

    # RHS of the constraints (provided by the user)
    b = [rhs1 - 21000, rhs2 - 21000, rhs3 - 21000, rhs4 - 21000]  # The inequalities are reversed to match the format of linprog

    # Bounds for variables (x and y must be non-negative)
    x_bounds = (0, None)
    y_bounds = (0, None)
    z_bounds = (0, None)
    a_bounds = (0, None)

    # Solve the linear programming problem
    result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds, a_bounds], method='simplex')

    if result.success:
        x = result.x[0]
        y = result.x[1]
        z = result.x[2]
        a = result.x[3]
        return x, y, z, a
    else:
        print("Solver failed:", result.message)
        raise Exception("No solution found.")

# Function to be called when the button is clicked
def on_solve_button_click():
    try:
        # Get the input values from the entry fields and convert to float
        rhs1 = float(entry_rhs1.get())
        rhs2 = float(entry_rhs2.get())
        rhs3 = float(entry_rhs3.get())
        rhs4 = float(entry_rhs4.get())

        # Debugging: print the input values
        print(f"User input values: rhs1 = {rhs1}, rhs2 = {rhs2}, rhs3 = {rhs3}, rhs3 = {rhs3}")

        # Solve the problem
        x, y, z, a= solve_truck_problem(rhs1, rhs2, rhs3, rhs4)

        # Debugging: print the results
        print(f"Solved values: x = {x}, y = {y}, z = {z}, a = {a}")

        # Display the result
        result_label.config(text=f"Optimal stacks of Runecloth:\nDarkspear Trolls: {x:.2f}\nOrgrimmar: {y:.2f}\nThunder Bluff: {z:.2f}\nUndercity: {a:.2f}\n\nTotal: {a + x + y + z:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for RHS.")
    except Exception as e:
        # Handle any other errors such as solver failure
        messagebox.showerror("Solver Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Reputation Donation Optimizer")

# Create and place the input labels and entry fields
label_rhs1 = tk.Label(root, text="Enter reputation with Darkspear Trolls:")
label_rhs1.pack()

entry_rhs1 = tk.Entry(root)
entry_rhs1.pack()

label_rhs2 = tk.Label(root, text="Enter reputation with Orgrimmar:")
label_rhs2.pack()

entry_rhs2 = tk.Entry(root)
entry_rhs2.pack()

label_rhs3 = tk.Label(root, text="Enter reputation with Thunder Bluff:")
label_rhs3.pack()

entry_rhs3 = tk.Entry(root)
entry_rhs3.pack()

label_rhs4 = tk.Label(root, text="Enter reputation with Undercity:")
label_rhs4.pack()

entry_rhs4 = tk.Entry(root)
entry_rhs4.pack()

# Create a button to solve the problem
solve_button = tk.Button(root, text="Solve", command=on_solve_button_click)
solve_button.pack()

# Label to display the results
result_label = tk.Label(root, text="Optimal stacks of Runecloth will be shown here.")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()