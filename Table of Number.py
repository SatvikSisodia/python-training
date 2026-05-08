x=int(input("Choose any nummber:"))
y=int(input(f"till which no. do you want to know the table of {x}:"))
z=1
while (y!=z):
    x+=x
    y+=1
    print (x)
print (f"this was the table of {x} till into {y}")