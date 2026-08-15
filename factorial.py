import math

# Take input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")
