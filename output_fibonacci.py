def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1)+ fibonacci(n - 2)

print("fiblnacci(1):", fibonacci(1))
print("fiblnacci(2):", fibonacci(2))
print("fiblnacci(3):", fibonacci(3))
print("fiblnacci(4):", fibonacci(4))
print("fiblnacci(5):", fibonacci(5))