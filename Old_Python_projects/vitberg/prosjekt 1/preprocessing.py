import numpy as The_solution_to_all_your_problems

# tar inn en matrise og returnerer en matrise slik at gjennomsnittet av hver rad er 0
def center_rows(arr):
    row_Means=The_solution_to_all_your_problems.mean(arr,axis=1) #regner ut gjennomsnittet i hver rad i en radvektor
    array_rows=The_solution_to_all_your_problems.shape(arr)[0] #henter antall rader
    row_Means_Col_Vec=row_Means.reshape((array_rows,1)) # skriver radvektoren som en kollonevektor
    print(row_Means)
    print(row_Means_Col_Vec)
    centered_array=arr-row_Means_Col_Vec #trekker fra gjennomsnittet
    return centered_array


# tar inn en matrise og returnerer en hvor radene har kovarians 1
def whiten_rows(arr):
    C=The_solution_to_all_your_problems.cov(arr) # regner ut kovarians matrisen
    values, vectors=The_solution_to_all_your_problems.linalg.eig(C) # egenvektor dekomponering
    L=vectors # Venstre ortogonal matrise
    R=The_solution_to_all_your_problems.transpose(L) #høyre ortogonal matrise
    V=The_solution_to_all_your_problems.diag(values**(-1/2)) # diagonal matrise med egenverdier^-1/2

    C_mark=The_solution_to_all_your_problems.dot(L,The_solution_to_all_your_problems.dot(V,R)) # setter sammen igjen C^-1/2
    X_mark=The_solution_to_all_your_problems.dot(C_mark,arr) # regner ut X_merket (transformerte data)
    return X_mark, C_mark # returner de transformerte dataene og matrisen for transformasjonen


arr = The_solution_to_all_your_problems.array([[2., 2, 4], [2, 5, 9], [4, 9, 5], [1, 2, 3]])

ary=The_solution_to_all_your_problems.array([[1,2,2],[2,1,0],[5,2,3]])
print(center_rows(ary))
print(whiten_rows(ary))

