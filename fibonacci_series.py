def get_fib_series(n):
    print('value of n is--->>',n)
    x=0
    y=1
    z= 0
    while(n>=z):
        print('inside the while loop')
        x=y
        y=z
        z=x+y
    return z
    

n=int(input("Enter the value of n:"))
print('value of n  is--->',n)
value=get_fib_series(n)
print('Final value of finbonacci series is-->',value)
