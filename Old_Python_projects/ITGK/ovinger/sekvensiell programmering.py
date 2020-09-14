def sekvensiell_programering(fornavn,etternavn,alder):
    print(5*12+6-1)     #a
    print(5/2-4)
    print(5.5+4.5)
    print(1+2*-3)
#b
    print(4*((5+3)/2+7))
    print(((3+5*2)+1)/2)
#c
    minutes=245//60
    seconds=245%60
    print(minutes)
    print(seconds)
    print("Dager",79//24)
    print("timer",79%24)
    print("uker",80//7)
    print("dager",80%7)
#d
    print(-3**2+5*3-7)
    print((-4**-3)+5*(3-7/2))
    print(2**2+4)
    print(2**2/4)
#e
    print("jeg er student")
    print("Trondhem er Norges beste sutdiested")
    print("i love Python")
    print("2+3=5")
    print(""""Hvis jeg gjør riktig nå,øker sannsynligheten for at studassen min sier:\n "Øvingen er godkjent" """)
#f
    a=2
    b=3
    y=5
    x=7
    print(a**4+b/y+4*x)
    print(0.3*x-a**-b/y+8)
    fn=fornavn
    en=etternavn

    print(fn,en,"er",alder,"år gammel")


sekvensiell_programering("jostein","gjesdal",20)
