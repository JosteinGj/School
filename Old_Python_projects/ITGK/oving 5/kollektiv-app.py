def billett(age, bike):
    if bike.upper() == "J":
        if age < 5:
            return print(50)
        elif age <= 20:
            return print(70)
        elif age <= 25:
            return print(100)
        elif age <= 60:
            return print(130)
        else:
            return print(50)
    else:
        if age < 5:
            return print(0)
        elif age <= 20:
            return print(20)
        elif age <= 25:
            return print(50)
        elif age <= 60:
            return print(80)
        else:
            return print(0)
ferdig="n"
while ferdig.upper()!="J":
    age=int(input("hvor gammel er passasjeren? "))
    bike=input("har passasjeren med seg sykkel? (J/N) ")
    billett(age,bike)
    ferdig=input("er du ferdig med handelen? ")