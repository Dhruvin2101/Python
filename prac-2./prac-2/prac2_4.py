                                             # Built a calculator

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("enter the operator: ")


def calculator(num1,num2,operator):
    if(operator == '+'):
        return num1 + num2
    elif(operator == '-'):
        return num1 - num2
    elif(operator == '/'):
        return num1 / num2
    elif(operator == '*'):
        return num1 * num2
    else:
        print("Enter the correct operator")
    
result = calculator(num1,num2,operator)
print("the result is",result)