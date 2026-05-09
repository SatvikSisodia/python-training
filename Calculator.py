def calc():
    operation=input("would you like to add, subtract, multiply or divide(Please write in smallcase)?")
    if (operation=="add"):
        print(f"The sum is {x+y}")
    elif (operation=="subtract"):
        print(f"The difference is {x-y}")
    elif (operation=="multiply"):
        print(f"The result is {x*y}")
    elif (operation=="divide"):
        print(f"The quotient is {x/y}")
    else:
        print("Invalid input")
b=1
while (b==1):
    x=int(input("enter any number:"))
    y=int(input("enter another number:"))
    calc()
    b=int(input("Press the number 1 if you want to continue with a new set of numbers, otherwise press any number."))
print("Thank you")