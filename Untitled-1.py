string=input("enter the string")
length=len(string)
i=0
while i<length:
    j=0
    while j<=i:
        print(string[j],end=" ")
        j=j+1
    print()
    i=i+1