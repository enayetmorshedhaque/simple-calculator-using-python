def welcome_text():
    print("Simple Calculator Using Python")

def section_divider():
    print("------------------------------")

def operators_list():
    print("Select Your Option")
    section_divider()
    operators = ['+', '-', '*', '/', '%']
    for i in range(len(operators)):
        print(f"{i+1}. {operators[i]}")
    print(f"{len(operators)+1}. Exit")

def input_numbers():
    input_one = float(input("Enter Number One: "))
    section_divider()
    input_two = float(input("Enter Number Two: "))
    section_divider()
    return input_one, input_two

def add(a, b):
    print(f"{a} + {b} = {(a + b)}")

def sub(a, b):
    print(f"{a} - {b} = {(a - b)}")

def mul(a, b):
    print(f"{a} * {b} = {(a * b)}")

def div(a, b):
    if(b == 0):
        print("Oooppss... Invalid Operation")
    else:
        print(f"{a} / {b} = {(a / b)}")

def mod(a, b):
    print(f"{a} % {b} = {(a % b)}")


#main program starts here
section_divider()
welcome_text()
section_divider()

print("\n\n")

exit_program = False
while not exit_program:
    operators_list()
    section_divider()

    choice = input("Enter your choice: ")
    section_divider()

    if choice == '1':
        a, b = input_numbers()
        add(a,b)
        section_divider()
        print("\n")

    if choice == '2':
        a, b = input_numbers()
        sub(a,b)
        section_divider()
        print("\n")
    
    if choice == '3':
        a, b = input_numbers()
        mul(a,b)
        section_divider()
        print("\n")

    if choice == '4':
        a, b = input_numbers()
        div(a,b)
        section_divider()
        print("\n")

    if choice == '5':
        a, b = input_numbers()
        mod(a,b)
        section_divider()
        print("\n")

    if choice == '6':
        print("Exiting the program.....")
        section_divider()
        break

exit_program = True
