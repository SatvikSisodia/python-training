startstop=2
while(startstop!=1):
    marks=[93,87,49,68,91,81,79,64,76,43,100,56,89,95,87]
    names=["aarav j","aarav s", "aayansh s", "daksh s", "jiaana g", "kabir j", "manth b", "myra s", "medhansh s", "paridhi g", "raghav m", "samaira g", "uddhav j", "vihaan a", "zohan k"]
    rangestart=int(input("which roll no. do you want to know the marks of? there are a total of 15 students"))
    if (rangestart<15):
        x=rangestart-1
        print(names[x])
        print(marks[x])
        startstop=int(input("type the no. 1 if want to stop. or else, press any number"))
    else:
        print("invalid answer")
        startstop=int(input("type the no. 1 if want to stop. to continue, press any number"))
