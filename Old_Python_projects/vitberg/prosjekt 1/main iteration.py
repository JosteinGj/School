import numpy as np
# tar inn en matrise og returnerer en matrise med normaliserte rader
def normalize_rows(arr):
    norms=np.linalg.norm(arr,axis=1) # lager en radvektor med normen til hver rad
    nrows=np.shape(arr)[0] #henter antall rader i matrisen
    col_vec_norms=norms.reshape((nrows,1)) #skriver radvektoren til en kollonevektor
    normalized_array=arr/col_vec_norms # bruker broadcasting til å normalisere radene i matrisen
    return normalized_array
# (W_1)ij i er rader j er kollonner
def Measure_of_Convergence(W1,W2):
    weights=np.multiply(W1,W2) # multipliserer vekt matrisene elementvis
    weight_vector=1-np.absolute(np.sum(weights,axis=1)) #en vektor med 1- absoluttverdien av summen av alle vektene på hver rad i weights
    return max(weight_vector) # returner maks verdien i weight vector

# kose funksjon som gjør hele den over på 1 linje
# def moc(w1,w2): return np.max( 1 - np.absolute( np.sum( np.multiply( w1,w2 ), axis=1)))

def fast_ICA(Z, signals_to_find, tol = 1e-10, max_iter = 100):





arr = np.array([[1, 1, 1, 1], [2, 5, 9, 2], [4, 9, 5, 2], [2, 2, 2, 2]])
normalize_rows(arr)
a1=np.array([[1,1],[1,-1]])
a2=np.array([[1,-2],[2,1]])
a1=np.multiply(1/np.sqrt(2),a1)
a2=np.multiply(1/np.sqrt(5),a2)
print(Measure_of_Convergence(a1,a2))
print(moc(a1,a2))

