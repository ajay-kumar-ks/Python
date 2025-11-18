def isPowerOfTwo(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed.")

    if n == 0:
        return False

    while n % 2 == 0:
        n = n // 2    
        if n == 1:
            return True

    return False

val = int(input("Enter a positive number: "))

try:
    if isPowerOfTwo(val):
        print(val, "is power of two")
    else:
        print(val, "is not a power of 2")
except ValueError as e:
    print(e)
