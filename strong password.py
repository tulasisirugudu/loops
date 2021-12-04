password=int(input("enter the number"))
if len(password)==1 and len(password)<=8:
    if "$" in password or "@" in password or "#"in password:
        if"0"or"9" in password:
            if "a" or "z" in password:
                print("strong password")
            else:
                print("weak password")
        else:
            print("wrong password")
    else:
        print("wrong")
else:
    print("nothing")