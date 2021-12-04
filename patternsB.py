# 5 4 3 2 1
# 5 4 3 2
# 5 4 3 
# 5 4 
# 5
n=int(input("enter the rows"))
i=1
while (i<=n):
    j=n
    while(j>=i):
        print(j,end="")
        j=j-1
    i=i+1
    print()