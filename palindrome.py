x=int(input("enter any number"))
y=str(x)
length=len(y)
length1=length-1
a=0
b="true"
c=length1
while (c>a):
    if (y[a]!=y[c]):
        b="false"
        break
    a+=1
    c-=1
print(b)