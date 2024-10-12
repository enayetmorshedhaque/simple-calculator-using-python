# Python Simple Calculator

This Python program is a command-line based simple calculator that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and modulus. The user can select operations by inputting numbers associated with the specific operators.

## Features

- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`) (handles division by zero)
- **Modulus** (`%`)
- **Exit** the program

## How It Works

1. **Select an operator**: The user selects one of the following operations by entering the corresponding number:
   - 1 for Addition
   - 2 for Subtraction
   - 3 for Multiplication
   - 4 for Division
   - 5 for Modulus
   - 6 to Exit the program
2. **Input numbers**: After selecting an operator, the user is prompted to enter two numbers.
3. **View the result**: The program displays the result of the selected operation.
4. **Continue or exit**: The user can choose to continue performing calculations or exit.

### Example

```bash
------------------------------
Simple Calculator Using Python
------------------------------


Select Your Option
------------------------------
1. +
2. -
3. *
4. /
5. %
6. Exit
------------------------------
Enter your choice: 1
------------------------------
Enter Number One: 5
------------------------------
Enter Number Two: 3
------------------------------
5.0 + 3.0 = 8.0
------------------------------
```

## Error Handling

- The program handles **division by zero** and displays a message when the user attempts to divide or use modulus with zero.

## Requirements

- Python 3.x

## How to Run

- Copy the code into a Python file (e.g. `simple_calculator.py`)
- Run the Python script in your terminal or IDE:

```bash
python simple_calculator.py
```

- Follow the on-screen prompts to perform calculations.

## License

- This project is licensed under the MIT License.

Feel free to contribute to this project or report issues!
