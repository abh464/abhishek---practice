def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    previous_sum = fibonacci_series(n-1) + fibonacci_series(n-2)
    return previous_sum

n = 6
sum = fibonacci_series(n)
print("Fibonacci of ",n," is : ",sum)
