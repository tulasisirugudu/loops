num=int(input("emter the number"))
i=2
j=0
while i<=num/2:
    if num%i==0:
        j=1
        break
    i=i+1
if j==0:
    print("it is prime")
else:
    print("not a prime")
