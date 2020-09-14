from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
pensize(7)          # sett pennen 7 piksler tykk
pencolor("pink")    # sett pennefargen til rosa
bgcolor("grey")     # sett bakgrunnsfargen grå
fillcolor("purple") # sett fyllfargen lilla
# Tegner en fylt trekant
begin_fill()
forward(200)        # gå 100 piksler framover
left(120)           # drei 120 grader venstre
forward(200)
left(120)
forward(200)
end_fill()