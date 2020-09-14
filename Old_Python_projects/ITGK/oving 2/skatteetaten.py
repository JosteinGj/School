boligtype=input("hvilken type bolig leier du ut? (primær/sekundær/fritids)")
if boligtype=="primær":
    boligprosent = int(input("hvor mange prosent av boligen leier du ut?"))
    leieintekt = int(input("hva er din årlige leieinntekt?"))
    if boligprosent<50:
        print("skattefritt")
    else:
        if leieintekt<20000:
            print("skattefritt")
        else:
            print("skattepliktig beløp:",leieintekt)
elif boligtype=="sekundær":
    print("hele inntekten er skattepliktig")
else:
    friBoligAntall=int(input("hvor mange fritidsboliger leier du ut?"))
    leieintekt = int(input("hva er din årlige leieinntekt per bolig?"))
    bruk = input("bruker du fritidsboligen selv? (J/N)")
    pr_bolig=(leieintekt-10000)*0.85
    if bruk.upper()=="J":
        print("skattepliktig beløp per bolig:"+str(pr_bolig))
        print("Totalt skattepliktig beløp:"+str(pr_bolig*friBoligAntall))
    else:
        print("skattesats:",friBoligAntall*leieintekt)

