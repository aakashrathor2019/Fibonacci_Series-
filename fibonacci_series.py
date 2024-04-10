#Fibonacci Series Generate with mathematical recurrence 
def fibonacci_generator():
    a, b = 0, 1
    yield a
    yield b
    while True:
        if a <= b:
            a = a + b
            yield a
        else:
            b = a + b
            yield b

print("Enter the value of n:")
n = int(input())  # Convert input to integer
fib_gen = fibonacci_generator()
for i in range(n):
    print(next(fib_gen))
