
   #set inn et tak for hvor høyt du vil finne summen av alle tallene delelig med 3 eller 5
def multiple3n5():
    n=1                 #vi starter tellingen fra n=1
    tak=int(input("input a roof"))  #set inn et tak for hvor høyt du vil finne summen av alle tallene delelig med 3 eller 5
    list=[]             #etablerer en tom liste vi skal fylle med alle tall delelig på 3 eller 5
    while n < tak:        #mens vi regner på tall under taket
        if n%3==0 or n%5==0:    #hvis n er delelig på 3 eller 5 legg den til listen
            list.append(n)
        n+=1                    #inkrementerer n uavhenging av om tallet går opp i 3 eller 5
    return(sum(list)) #til slutt summerer vi alle tallene i listen
print(multiple3n5())