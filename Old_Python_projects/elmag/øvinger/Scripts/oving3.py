import numpy as np
import matplotlib.pyplot as matplot


def plot_sinus():
    x=np.linspace(0,2*np.pi,100)
    y=np.sin(x)
    g=np.cos(x)
    matplot.plot(x,g, label="cos(x)")
    matplot.plot(x,y,label="sin(x)")
    matplot.legend()
    matplot.xlabel("x")
    matplot.ylabel("f,g")
    matplot.title("kek")
    matplot.show()



plot_sinus()