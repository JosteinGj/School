avreise_tid = int(input("Dager til du skal reise? "))
student=input("er du student? (J/N)")
alder=int(input("skriv in din alder: "))
mini=199
ordi=440
if avreise_tid>13:

    print("da kan du få minipris til(billetten kan ikke refunderes eller endres")
    svar_minipris=input("ønsker du minipris billett? (J/N) ")
    if svar_minipris.upper()=="J" and student.upper()=="J":
        if alder<16:
            print("du kan få ordinær billett til: 165 kr")
            svar_spes=input("ønskes dette?(J/N")
            if svar_spes.lower()=="j":
                print("flott")
            else:
                print("da får du en minipris billet til ", mini)
        else:
            print(mini*0.9)
    elif svar_minipris.upper()=="J" and student!="J":
        print(mini)
    else:

        if student.upper()=="J":
            mil_sen = input("er du senior(60+) eller militær?")
            if alder<16:
                print("din pris:"+str(round(ordi*0.375,2))+"kr")
            elif mil_sen.upper()=="J":
                print("din pris: "+str(round(ordi*0.5,2))+"kr")
            else:
                print(ordi*0.75)
        elif alder<16:
            print(ordi*0.5)
        elif input("er du militær eller senior? (J/N)")=="J":
            print(ordi*0.75)
        else:
            print(ordi)

else:
        mil_sen = input("er du senior(60+) eller militær?")
        if student.upper()=="J":

            if alder<16:
                print("din pris:"+str(round(ordi*0.375,2))+"kr")
            elif mil_sen.upper()=="J":
                print("din pris: "+str(round(ordi*0.5,2))+"kr")
            else:
                print(ordi*0.75)
        elif alder<16:
            print(ordi*0.5)
        elif mil_sen.upper=="J":
            print(ordi*0.75)
        else:
            print(ordi)