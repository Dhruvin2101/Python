                    # Swapping between two numbers without using TemporaryVariable
a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
print(" ")

print("Before swapping: ",a,b)
print(" ")
(a,b) = (b,a)       # logic
print("After swapping: " ,a,b)