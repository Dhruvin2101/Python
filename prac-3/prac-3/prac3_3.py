def gcd(a, b):

    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
        
    return result


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD of {a} and {b} is {gcd(a, b)}")

