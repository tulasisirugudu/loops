n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j=j+1
    j=i
    while j>0:
        print(j,end=" ")
        j=j-1
    j=2
    while j<i+1:
        print(j,end=" ")
        j+=1
    print()
    i=i+1

