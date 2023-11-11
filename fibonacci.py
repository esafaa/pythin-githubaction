import sys

def get_input():
    try:
        # Attempt to read input if running interactively
        return int(input("How many terms? "))
    except EOFError:
        # Handle EOFError by providing a default value
        print("No input provided. Using default value.")
        return 5  # Change this to the desired default value

def fibonacci(n):
    # Implementation of the Fibonacci sequence calculation
    # ...

# Get the number of terms either from user input or use a default value
nterms = get_input()

# Call your Fibonacci function with nterms
fibonacci(nterms)
