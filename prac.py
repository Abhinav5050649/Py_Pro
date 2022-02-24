def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

def main():
    print("Enter two numbers")
    x = int(input("X: "))
    y = int(input("Y: "))

    s = input("Enter operation to perform: +, -, *, %, /: ")

    if (s == '+'):
        print("Sum of numbers is ", (x + y))
    elif (s == '-'):
        print("Difference of numbers is ", (x - y))
    elif (s == '*'):
        print("Product of number is ", multiply(x, y))
    elif (s == '/'):
        print("Quotient of the operation is ", divide(x, y))
    elif (s == '%'):
        print("Remainder of the operation is ", modulo(x, y))
    else:
        print("Please Enter proper operator!")

main()