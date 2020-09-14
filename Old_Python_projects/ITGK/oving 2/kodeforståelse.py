def part1():
    tall_1 = 2
    tall_2 = int(input("Skriv inn et tall: ")) #feil: input behanldes som et tall
    if tall_2==0:
        print("error division by zero")
    else:
        resultat = tall_1 // tall_2
    print(resultat)
def part2():
    a = 2
    b = 3
    if (b < a or b % a==0):#dersom b er mindre enn a eller b er delelig på a
        b = a + b #skriv b= a+b
    else:
        a = a * b #ellers skriv a=a*b
    print("a: ", a)
    print("b: ", b)
#dersom vi setter inn a=3 og b=3 får vi at b<a=true => b=a+b

part2()