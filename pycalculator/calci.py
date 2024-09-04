from tkinter import *    #using Tkinter for GUI Interface 

# Function to evaluate the expression and display the result
def evaluate():
    try:
        operator = operator_var.get()
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result_var.set("Error: Division by zero")
                return
        elif operator == '%':
            result = num1 % num2
        else:
            result_var.set(f"{operator} is not a valid operator!")
            return

        result_var.set(f"Result: {result}")

    except ValueError:
        result_var.set("Error: Invalid input")

# Creating the main window
root = Tk()
root.title("Daily Calci-Use")

# Creating and placing widgets
Label(root, text="Enter first number:").grid(row=0, column=0, padx=5, pady=5)
num1_entry = Entry(root)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Enter second number:").grid(row=1, column=0, padx=5, pady=5)
num2_entry = Entry(root)
num2_entry.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Enter an Operator (+, -, *, /, %):").grid(row=2, column=0, padx=5, pady=5)
operator_var = StringVar()
operator_entry = Entry(root, textvariable=operator_var)
operator_entry.grid(row=2, column=1, padx=5, pady=5)

result_var = StringVar()
result_label = Label(root, textvariable=result_var)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

calculate_button = Button(root, text="Calculate", command=evaluate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
