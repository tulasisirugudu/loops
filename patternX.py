n=int(input("enter the number"))
i=0
while(i<=n):
    j=0
    while(j<=n-i):
        print(" ",end=" ")
        j=j+1
    j=0
    while(j<=(2*i-1)-1):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
