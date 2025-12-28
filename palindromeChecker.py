z=[]
x=int(input("write the no. of students in your class"))
y=(input("write the grade of student"))
z.append(y)
x-=1
while (x==0):
    y=input("write the grade of next student")

    z.append(y)
    x-=1
