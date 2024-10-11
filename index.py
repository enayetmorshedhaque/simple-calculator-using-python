def operators_list():
    
    operators = ['+', '-', '*', '/', '%']

    for i in range(len(operators)):
        print(f"{i+1}. {operators[i]}")

    print(f"{len(operators)+1}. Exit")

def input_numbers():
    
    input_one = float(input("Enter Number One: "))
    input_two = float(input("Enter Number Two: "))
    
    return input_one, input_two

def section_divider():
    print("------------------------------")


print("\nSimple Calculator Using Python")
section_divider()

exit_program = False

while not exit_program:
    number_one, number_two = input_numbers()
    print("------------------------------")
    operators_list()
    print("------------------------------")
    choice = int(input("Enter Your Choice: "))
    print("------------------------------")

    if choice == 1:
        print(f"Result is: {number_one + number_two}")  # Addition
        print("------------------------------")

    elif choice == 2:
        print(f"Result is: {number_one - number_two}")  # Subtraction
        print("------------------------------")

    elif choice == 3:
        print(f"Result is: {number_one * number_two}")  # Multiplication
        print("------------------------------")

    elif choice == 4:
        if number_two != 0:
            print(f"Result is: {number_one / number_two}")  # Division
            print("------------------------------")
        else:
            print("Error: Division by zero is not allowed.")
            print("------------------------------")
    elif choice == 5:
        if number_two != 0:
            print(f"Result is: {number_one % number_two}")  # Modulus
            print("------------------------------")
        else:
            print("Error: Modulus by zero is not allowed.")
            print("------------------------------")

    elif choice == 6:
        exit_program = True  # Exit the loop and program
        print("Exiting the program...")
        print("------------------------------")

    else:
        print("Invalid choice, please try again.")
        print("------------------------------")
