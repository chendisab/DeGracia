def divide_numbers(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def power(base, exponent):
    return base ** exponent

def get_remainder(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a % b

def summation(start, end):
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        choice = input("Enter your choice: ").upper()

        if choice == "D":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number (denominator): "))
            result = divide_numbers(a, b)
        elif choice == "E":
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            result = power(base, exponent)
        elif choice == "R":
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number (denominator): "))
            result = get_remainder(a, b)
        elif choice == "F":
            start = int(input("Enter the first number: "))
            end = int(input("Enter the second number (must be greater than first): "))
            result = summation(start, end)
        elif choice == "X":
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()
