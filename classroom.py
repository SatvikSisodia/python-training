students=["aarav j", "aarna s", "aayansh s", "aayra b", "ayaansh g", "dushyant b",]
marks=["not assigned", "not assigned", "not assigned", "not assigned", "not assigned","not assigned"]
x="hello"
while (x!="stop"):
    length=len(marks)
    x=input("hello! what would you like to do(know marks, add student, change marks, or stop)")
    if (x=="know marks"):
        y=int(input("what roll no.?"))
        z=y-1
        if (y>=length):
            print(students[z]+"-"+marks[z])
        else:
            print("invalid.")