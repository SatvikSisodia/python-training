data=[]
x=0
name=input("State your name")
data.append(name)
age=int(input("Enter your age"))
data.append(age)
if (age<18):
    while (x==0):
        grade=int(input("What grade are you in?"))
        if (grade<13):
            print("Ok, "+name+".")
            data.append(grade)
            print(data)
            x+=1
        else:
            print("invalid answer.")
else:
    occupation=input("are you in college, post graduation or job?")
    data.append(occupation)
    print(data)
    
