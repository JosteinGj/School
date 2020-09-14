def Factor(n):
    i = 2
    Factors = []
    while i * i <= n:          #alle primtallsfaktorer av n er mindre eller lik kvadratroten av n
        if n % i != 0:         #vi sjekker om vi kan dele på i, dersom resten er ulik 0 er i ikke en faktor av n
            i += 1             #vi øker i for å sjekke om i+1 er en faktor ettersom i ikke var det
        else:
            n //= i   #er nå vist i en faktor av n, vi deler derfor n på i slik at vi nå tester på n=n/i
            Factors.append(i) #vi setter i inn i listen siden der er en faktor og øker ikke i slik at hvis i fortsatt er en faktor kan vi teste den
    if n>1:
        Factors.append(n) #når vi har testet alle i opp til kvadratroten av n og da må n være lik 1 eller den siste faktoren i n
    return Factors
print(Factor(20001))