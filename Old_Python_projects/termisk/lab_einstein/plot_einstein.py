import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

def einstein_spesific_heat(Etemp):
    return (3*8.31446*(Etemp)**2)*(np.exp(Etemp))/(np.exp(Etemp)-1)**2

def einstein_plot_from_file(file,einsteintemp):
    table=np.loadtxt(file,delimiter=",")
    table=table.transpose()
    temps = table[0]
    spesificHeat = table[1]*4.184
    vals=np.linspace(100,1200,10000)
    plt.plot(temps,spesificHeat,".")
    plt.plot(vals,einstein_spesific_heat(einsteintemp/vals))
    plt.plot(vals, einstein_spesific_heat(100/ vals))
    plt.show()
    return True

def einstein_plot_from_file_fluor(file,einsteintemp):
    table=np.loadtxt(file,delimiter=",")
    table=table.transpose()
    temps = table[0]
    spesificHeat = table[1]-8.31446
    vals=np.linspace(100,1200,10000)
    plt.plot(temps,spesificHeat,".")
    plt.plot(vals,einstein_spesific_heat(einsteintemp/vals)+8.31446)
    plt.plot(vals, einstein_spesific_heat(400 / vals)+8.31446)
    plt.show()
    return True

def einstein_plot_from_array(array,einsteintemp):
    temps=array[0]
    spesific_heat=array[1]
    vals = np.linspace(10,1000,100000)
    plt.plot(temps,spesific_heat,".")
    plt.plot(vals,einstein_spesific_heat(einsteintemp/vals))
    plt.show()
    return True

def gram_to_mol(file,molarmass):
    table=np.loadtxt(file,delimiter=",")
    table=table.transpose()
    table[1]=table[1]*molarmass
    return table

def cal_to_joule_tabell(table):
    table[1]=table[1]*4.184
    return table

def cal_to_joule(file):
    table=np.loadtxt(file,delimiter=",")
    table=table.transpose()
    table[1]=table[1]*4.184
    return table
Al_molar_mass=26.981538
einstein_plot_from_array(cal_to_joule_tabell(gram_to_mol("aluminumtabell2.txt", Al_molar_mass)), 293)
einstein_plot_from_array(cal_to_joule("aluminumtabell.txt"),293)
einstein_plot_from_file_fluor("fluortabell.txt",300)
#einstein_plot_from_array(cal_to_joule("aluminumtabell.txt"),900)
print(einstein_spesific_heat((1325/879.4))/4.184,np.exp(1))
einstein_plot_from_file("einstein_tabell.txt",1325)

# endringen i varmekapasiteten endres ved høye tempraturer skyldes
# nok at flere frihetsgrader kommer inn i spill
# vår modell tar ikke hensyn til dette ettersom

# Cvm for F_2 ser ut til å være betydelig høyere enn for aluminium.
# sannsynligvis pga rotasjonsfrihetsgradene.
