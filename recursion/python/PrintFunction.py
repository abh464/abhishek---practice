def print_number(n):
    if n <= 0:
        return
    print("value of n: ",n)
    print_number(n-1)

print_number(5)