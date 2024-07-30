
str = input("Enter a sentence: ")

digit=letter=uppercase=lowercase=space=0

for char in str:
    if char.isdigit():
        digit = digit + 1

    elif char.isalpha():
        letter = letter + 1     
        
        if char.islower():
            lowercase = lowercase + 1

        elif char.isupper():
            uppercase = uppercase + 1

    elif char.isspace():
        space = space + 1

    else: 
        print("Please check what you have entered ")

print("THe number of digits are: ", digit)
print("THe number of letters are: ", letter)
print("THe number of Lowercase are: ", lowercase)
print("THe number of Uppercase are: ", uppercase)
print("THe number of Space are: ", space)

