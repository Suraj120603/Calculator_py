def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Print options for the user
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Dictionary for operation names
operation = {1: "added", 2: "subtracted", 3: "multiplied", 4: "divided"}

# Start loop for input processing
while True:
    choice = int(input("Choose operation (1/2/3/4): "))

    # Validate the choice input
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice, please select 1, 2, 3, or 4.")
        continue

    n = int(input(f"Enter the total number of values to be {operation[choice]}: "))

    numbers = []
    for i in range(1, n + 1):
        a = float(input(f"Enter number {i}: "))
        numbers.append(a)

    if choice == 1:
        # Addition
        list_sum = 0
        for num in numbers:
            list_sum = add(list_sum, num)
        print(f"Result of addition: {list_sum}")

    elif choice == 2:
        # Subtraction
        list_sub = numbers[0]
        for num in numbers[1:]:
            list_sub = subtract(list_sub, num)
        print(f"Result of subtraction: {list_sub}")

    elif choice == 3:
        # Multiplication
        list_mul = 1
        for num in numbers:
            list_mul = multiply(list_mul, num)
        print(f"Result of multiplication: {list_mul}")

    elif choice == 4:
        # Division
        list_div = numbers[0]
        for num in numbers[1:]:
            result = divide(list_div, num)
            if result == "Error! Division by zero.":
                print(result)
                break
            else:
                list_div = result
        else:
            print(f"Result of division: {list_div}")

