# Requirements:
# Take A Mathematical Expression: (x a number, z a number, y an operator).
# Numbers are Floating Points.
# Operations: (+, -, *, /).
##########################################################################
# Algorithm:
def main():
    # Take Expression from user.
    express = input("Enter a Mathematical Expression: ")
    # Split Expression, store in x,y,z
    x, y, z = express.split(" ")
    # Change x,z To Float.
    x = float(x)
    z = float(z)
    # Check Operation depending on y.
    check_n_operate(x, y, z)


# Operation Function.
def check_n_operate(no1, operator, no2):
    match operator:
        case "+":
            print(no1 + no2)
        case "-":
            print(no1 - no2)
        case "*":
            print(no1 * no2)
        case "/":
            print(no1 / no2)
        case _:
            print("Wrong Operator")


def divide(no1, no2):
    ...


if __name__ == '__main__':
    main()
