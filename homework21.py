def factorial(n):
    #               factorial of 0 is 1
    if n == 0:
        return 1
    #                  n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

user_input = input("Enter a non-negative integer to calculate its factorial: ")

try:
    number = int(user_input)

    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
