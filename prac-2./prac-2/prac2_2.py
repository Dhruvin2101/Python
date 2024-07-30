                                # Find the largst number between three numbers


num1 = int(input("enter a number1: "))
num2 = int(input("enter a number2: "))
num3 = int(input("enter a number3: "))

if((num1>num2) and (num1>num3)):
    print("The largest number is: "+num1)
    
elif((num2>num1)and(num2>num3)):
    print("The largest number is: "+num2)
    
else:
    print("The largest number is: "+num3)