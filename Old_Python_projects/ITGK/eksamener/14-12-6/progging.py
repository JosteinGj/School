import numpy as np
import math
def inputperson():
    details=[ input("Name: "),input("ID: "),input("weight: "),input("Size: ")]
    return details

def readDbFile(filename):
    file=open(filename)
    output=[]
    for lines in file:
        lines=lines.rstrip()
        data=lines.split(";")
        data[2],data[3]=int(data[2]),int(data[3])
        output.append(data)
    return output


def printMemberList(db):
    print("{: <15}{: <9}{: <5} {} {: <4}".format("Name","ID_Nr","Vekt","kg.","Screensize"))
    for i in range(len(db)):
        print("{0[0]: <15}{0[1]: <9} {0[2]: <5}kg  "
              "{0[3]: <4} squarefeet".format(db[i]))



def addperson(filename):
    newbie=inputperson()
    file=open(filename,"a")
    file.write("\n{0[0]};{0[1]};{0[2]};{0[3]}".format(newbie))
    file.close()
    database=readDbFile(filename)
    return database

def feet2sec(feet):
    if feet>4000:
        return 10+(feet-4000)/200
    elif feet>3000:
        return (feet-3000)/100
    else:
        return 0
def weatherstats(weatherData):
    wd=np.array(weatherData)
    maxtemps=list(wd.transpose()[0])
    mintemps=list(wd.transpose()[1])
    nedbør=list(wd.transpose()[2])
    print("there are {} days in the period".format(len(weatherData)))
    print("max temp was {} C on day {}".format(max(maxtemps),(maxtemps.index(max(maxtemps))+1)))
    print("min temp was {} C on day {}".format(min(mintemps),(mintemps.index(min(mintemps))+1)))
    print("downpour was {} C on day {}".format(max(nedbør),(nedbør.index(max(nedbør))+1)))

def coldestdays(weatherdata):
    if len(weatherdata)<3:
        print("invalid input: input to short")
        return None
    wd=np.array(weatherdata)
    mintemps=list(wd.transpose()[1])
    coldcombo=math.inf
    comboday=-1
    for i in range(len(mintemps)-2):
        if sum(mintemps[i:i+2])/3<coldcombo:
            coldcombo=sum(mintemps[i:i+2])/3
            comboday=i
    return comboday


we=[[1,2,3],[3,9,1],[4,3,2],[5,3,2],[1,2,3],[8,1,6]]
print(coldestdays(we))


def extradays(extra,weather):
    extra=extra.split(",")
    extra[0],extra[1],extra[2]=extra[0][3:],extra[3:],extra[:-2]
    weather.append(extra)
    return weather





