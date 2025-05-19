#this will ask user for an input with a prompt "Enter a number" and then print that number

a = input("Enter a number: ") 
print(a)

#------------------------------

# this will ask user for an input with a prompt "Enter your name" and then print that number

b = input("Enter your name: ")
print(b)

#------------------------------

c = input("enter a number") # input function takes any input value as a string by default

# print(3 + c)  simply writing this will give TypeError: unsupported operand type(s) for +: 'int' and 'str'

c = int(c) # first we have to convert the input value which user gonna input to an integer   

print(3 + c) # now the input will be taken as an integer