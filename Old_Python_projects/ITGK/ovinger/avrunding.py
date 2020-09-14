n=input("enter a nummber")
inverse=n[::-1]
roundup=["5","6","7","8","9"]
list=(list(inverse))


for a in inverse:
    if a in roundup:
        print(a)


