str = input("enter the list elements with space:  ")    
my_list = str.split()
print("The Orignal list: -->  ",my_list)
print("")

my_set = set(my_list)
updated_list = list(my_set)
print("the list without duplicates: --> ",updated_list)