def read_from_file(filename):
    file=open(filename)
    return file.read()
def make_dict_CSV(filename):
    text=read_from_file(filename)
    output={}
    for i in text.splitlines():
        items=i.split(",")
        output[items[0]]=items[1]
    return output
def åpnestudier(filename):
    dictionary=make_dict_CSV(filename)
    counter=0
    åpnestudier_liste=[]
    for studie in dictionary:
        print(dictionary[studie])
        if "Alle" in str(dictionary[studie]):
            counter+=1
            åpnestudier_liste.append(studie)
    return (counter, åpnestudier_liste)
print(åpnestudier("poenggrenser_2011.csv"))

def avg_NTNTU(filename):
    dictionary=make_dict_CSV(filename)
    temp=[]
    for key in dictionary:
        if key[1:5]=="NTNU":
            if dictionary[key]=="Alle":
                dictionary[key]=0
                temp.append(dictionary[key])
            else:
                temp.append(float(dictionary[key]))
    return sum(temp)/len(temp)
avg_NTNTU("poenggrenser_2011.csv")
