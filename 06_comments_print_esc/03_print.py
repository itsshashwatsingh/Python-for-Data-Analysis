# print('hello ' world ') this will throw error

# but if we have to print ' in our text we use \' escape sequence 

print('hello \' world') 
#output-> hello ' world

# we can also print space in our text without giving any space but using '' ,'' instead where '' contains the text 

print('hello','world','5')
#output->hello world 5


# can we overwrite these default function ? yes we can

# we can print actual , instead of space in place of , using sep

print('hello','world','5',sep =",") #output -> hello,world,5

# with this we can print actual , or any thing inside '' will be printed in place of space

print('hello','shashwat','255',sep="/") #outpuut -> hello/world/255

# if we want to print text in multiple lines you can alway use multiple print statement

print("hi how are you")
print("my name is shashwat")

# can we overwrite these default function ? yes we can

# we can append multiple print statement with "(any thing like , / ,space etc)"in between in a single line

print('hello',end = ",") # in end=" " here " " can store value such as a b c d 1 2 3 /  , .. etc
print('world')
#output -> can append multiple print statements in a single line

print('hello',end =" ..//433..")
print('world')
# output-> hello ..//433..world