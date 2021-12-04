n=int(input("enter the number"))
i=0
while(i<=n):
    j=n
    while(j>i):
        print(n-i,end="")
        j=j-1
    print()
    i=i+1