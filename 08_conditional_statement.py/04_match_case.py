# we can use match case instead of if elif else statement as well 

b = int(input("Enter a number between 1  and 10"))

match b:
    case 1 : print("you won a car")

    case 4 : print("you won a camera")

    case 5: print("you won 5 $")

    case _: print("better luck next time")

    # this new style of writing might not availabe in older version of python