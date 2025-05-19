# rules to write strings litrals in python 

'''
#this will throw SyntaxError: invalid syntax

print("hey how are" 
 you doing ")
 '''

# correct way

print("hey how are you doing")

# but if we want to print a text in two different lines 
# we can use Escape Sequence

print("hey how are you doing\nhope doing fine")

# output-> hey how are doing
#          hope doing fine

# but sometime \n creates confusion 

#here i want to print \ in my string but getting different output

print ("how are you \nice ?") # output -> how are you
#                                         ice ?

# to avoid this confusion we use different escape sequence like \\ double backslash to print  \ single backslash

print("how are you doing\\nice ?") # output-> how are you doing \nice ?


# can also add tab spaces in your code
print("This is a tab\tcharacter.") # output-> this is a tab    character.