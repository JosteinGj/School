def Factor(n):
    i = 2
    factors = []
    while i * i <= n:          #alle primtallsfaktorer av n er mindre eller lik kvadratroten av n
        if n % i != 0:         #vi sjekker om vi kan dele på i, dersom resten er ulik 0 er i ikke en faktor av n
            i += 1             #vi øker i for å sjekke om i+1 er en faktor ettersom i ikke var det
        else:
            n //= i   #er nå vist i en faktor av n, vi deler derfor n på i slik at vi nå tester på n=n/i
            factors.append(i) #vi setter i inn i listen siden der er en faktor og øker ikke i slik at hvis i fortsatt er en faktor kan vi teste den
    if n>1:
        factors.append(n) #når vi har testet alle i opp til kvadratroten av n og da må n være lik 1 eller den siste faktoren i n
    return factors
factorlist=[]
for n in range(1,21):
    factorlist.append(Factor(n))
print (factorlist)
factor2=[]
factor3=[]
factor5=[]
factor7=[]
factor11=[]
factor13=[]
factor17=[]
factor19=[]
for a in factorlist:
    factor2.append(a.count(2))