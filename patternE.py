# 10
# 10 20
# 10 20 30
# 10 20 30 40 
# 10 20 30 40 50
n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j*10,end=" ")
        j=j+1
    print()
    i=i+1
