import random
Random=random.randint(1,100)
guess=int(input("Hey! Guess the number:"))
x=1
while(Random!=guess):
    print("Nope!")
    if(guess>Random):
        print("The number is smaller.")
    elif(guess<Random):
        print("The number is larger.")
    guess=int(input("Try again:"))
    x+=1
print(f"You Win! It took you {x} tries!")