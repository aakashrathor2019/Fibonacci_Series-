def fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series with", num_terms, "terms:")
print(fibonacci(num_terms))
