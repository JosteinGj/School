# coding=utf-8
import random as rnd
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt  # Import plotting library
def draw(nums,n):
    li=[0]*n
    i=0
    while li[-1]==0:
        draw=rnd.randint(0,len(nums)-1)
        if nums[draw] not in li:
            li[i]=nums[draw]
            i+=1
    return li

dt = 0.1  # Time-step
T = 10  # Total integration time
nt = round(T / dt)  # Total number of time-steps
x = np.zeros((2, nt + 1))  # Make a matrix (array) with 2 rows and nt+1 columns called x
x[:, 0] = np.array([1, 0.2])  # Set the first column of x equal to [1,0.2] (the rest are still zero) this column is x_0 or the "intitial conditions"

def f(x):
    dx = -4 * x[1] * x[0] ** 2
    dy = 2 * x[0] ** 2 - 0.1 * x[1]
    return np.array([dx, dy])
def g(x):
    return np.array([(x[0] - 1) ** 2, (x[1] - 2) ** 2])
def dg(x):
    jacobian = np.zeros((2, 2))
    jacobian[0][0] = 2 * x[0]
    jacobian[1][1] = 2 * x[1]
    return jacobian

def error(x, f, tol=10 ** -10):
    if f(x)[0] < tol and f(x)[1] < tol:
        return True
    else:
        return False

def newton(x, g, dg, tol=10 ** -10):
    k = 0
    print(error(x, g, tol))
    while not error(x, g, tol) and k < 1000:
        x = x - np.linalg.inv(dg(x)) @ g(x)
        print(x)
        k += 1
    return x

p = print
x0 = [2, 1]
print(newton(np.array([1, 1]), g, dg))

for it in range(0, nt):
    x[:, it + 1] = x[:, it] + dt * f(x[:, it])  # Forward Euler (you will modify this line to implement the backward Euler method with Newton iterations)

t = np.array(range(0, nt + 1)) * dt  # The discrete times that the solution is evaluated on (i.e., the horizontal axis of the following plot)
plt.plot(t, x[0, :], 'ro-', t, x[1, :], 'bx-')  # Plot both solution components, now using arraysimport matplotlib.pyplot as plt              # Import plotting library

############################## keksamen 2012
weatherdata={1:[1,0,30,3],2:[5,30,50,5],3:[3,120,65,7]}

def print_db(weather):
    print()# blank linje ikke viktig
    print("DAY | temp | rain | humidity | wind") #"Hardkodet" tabell teksten
    print("====+======+======+==========+=====")# "hardkodet" tabell formatering
    for day in weather: #for hver dag i dictionary, day itererer over alle nøkler i dictionaryen
        temp, rain,humidity,wind=weather[day] # google "python sequence unpacking" hvis du ikke skjønner dette
        print(f"{day:4}{temp:7}{rain:7}{humidity:11}{wind:6}") # pyformat.info har masse info om .format() som fungerer veldig likt som f-strings
#print_db(weatherdata) #ser ut som tallene i LF er litt feil, men det viktige er at dere får til å formatere teksten.
# tar inn en fil og splitter teksten på delimiter, returner alle utenom det første segmentet
def get_chapters(filename, delimiter):
    f=open(filename,"r") #åpne fil
    return f.read().split(delimiter)[1:] #les fil og split på delim returner alle uten om første segment

#går gjennom en liste med strenger og teller forekomster av word, returnerer en liste med telling fra hver sekvens
def count_words(string_list,word):
    count=[]# tellingens liste
    for string in string_list: # for hver tekstsegment
        count.append(string.lower().count(word.lower())) #legg tell forekomster av ord og legg til i count
    return count
def create_nums(num):# ubrukelig tullefunksjon som kan erstates av range(1,num+1)
    return [i for i in range(1,num+1)]

#teller forekomster av et ord i en tekstfil og plotter resultatet som funksjon av hvilken sekvens det forekommer i
def anal_book(filename,delim,word):
    chaps=get_chapters(filename,delim)
    words=count_words(chaps,word)
    plt.plot(range(1,len(chaps)+1),words,label=f"{word}")
    plt.xlabel("Chapters")
    plt.ylabel(f"number of {word}")
    plt.legend()
    plt.title("Word analysis")
    plt.show()

#anal_book("alice_in_wonderland.txt","CHAPTER","alice")
def anal_gangbang(file,delim,words): #kjører anal_book for flere ord.
    for word in words:
        anal_book(file,delim,word)

#print(len(get_chapters("alice_in_wonderland.txt","CHAPTER")))

