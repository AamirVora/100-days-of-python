from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operator_list = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
                }

def calculator():
    continue_user = True
    print(logo)
    num1 = int(input("Enter first number: "))

    while continue_user:
        operation = input("Enter operation: +, -, *, /: ")
        num2 = int(input("Enter second number: "))

        answer = operator_list[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        user_continue = input("Do you want to continue? (y/n): ").lower()

        if user_continue == "y":
            num1 = answer
        else:
            continue_user = False
            print("\n" * 20)
            calculator()

calculator()

