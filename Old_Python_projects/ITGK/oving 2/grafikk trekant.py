from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
retning=input("vil du ha spissen opp eller ned?")
pennfarge=input("hvilken farge vil du ha på streken din? gul,grønn turkis, brun eller orange")
fyllfarge=input("hvilken farge vil du ha på fyllet? gul,grønn turkis, brun eller orange")
if pennfarge=="gul":pencolor("#f1d282")
elif pennfarge=="grønn":pencolor("#c9d4b2")
elif pennfarge=="turkis":pencolor("#5cbec9")
elif pennfarge=="brun":pencolor("#90492d")
elif pennfarge=="orange":pencolor("#f58025")

bgcolor("#00509e")
if fyllfarge=="gul":fillcolor("#f1d282")
elif fyllfarge=="grønn":fillcolor("#c9d4b2")
elif fyllfarge=="turkis":fillcolor("#5cbec9")
elif fyllfarge=="brun":fillcolor("#90492d")
elif fyllfarge=="orange":fillcolor("#f58025")
pensize(7)          # sett pennen 7 piksler tykk

    # sett bakgrunnsfargen grå

# Tegner en fylt trekant
if retning.lower()=="opp":
    begin_fill()
    forward(200)        # gå 100 piksler framover
    left(120)           # drei 120 grader venstre
    forward(200)
    left(120)
    forward(200)
    input()
    end_fill()
else:
    begin_fill()
    forward(200)  # gå 100 piksler framover
    left(-120)  # drei 120 grader venstre
    forward(200)
    left(-120)
    forward(200)
    input()
    end_fill()