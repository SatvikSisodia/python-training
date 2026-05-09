print("Make your own pizza!!")
b=2
pizza_toppings=[]
while (b!="1"):
    b=input("name a topping, or press 1 if you are done.")
    if (b!="1"):
        pizza_toppings.append(b)
def pizza(list):
    if (len(pizza_toppings)!=0):
        a=0
        print("So your toppings are:")
        while (a<len(list)):
            print(f"{pizza_toppings[a]}, ", end=" ")
            a+=1
    else:
        print("Your pizza is plain cheese. Thank you!")
pizza(pizza_toppings)