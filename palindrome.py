x=int(input("enter any number to check for palindrome"))
y=str(x)
a=0
b="true"
c=len(y)
while (c>a):
    if (y[a]!=y[c]):
        b="false"
        break
    a+=1
    c-=1
print(b)