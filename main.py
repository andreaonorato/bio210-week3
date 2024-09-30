# Function to print the first 10 Fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]  # Start with the first two numbers in the Fibonacci sequence
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
        fib_sequence.append(next_number)
    
    return fib_sequence

# Print the first 10 Fibonacci numbers
first_100_fibonacci = fibonacci(100)
print(first_100_fibonacci)
