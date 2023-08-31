from art import logo


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


def calculator():
    print(logo)
    calculate_further = True

    first_number = float(input("What's the first number?: "))
    while calculate_further:

        operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
        for calculo in operations:
            print(calculo)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        choosen_function = operations[operation]
        answer = choosen_function(first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")
        calculate_further = input(
            f"Type \"y\" to continue calculating with {answer}, or type \"n\" to exit.: "
        )
        if calculate_further.lower() == "n":
            calculate_further = False
            calculator()
        else:
            first_number = answer


calculator()