import numpy as np


def wyznacznik_macierzy(A):
    wynik = 0
    indeksy = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]

    for ind in indeksy:
        Ac = A.copy()
        Ac = Ac[1:] #bez pierwszego rzedu

        height = len(Ac)

        for i in range(height):
            Ac[i] = Ac[i][0:ind] +Ac[i][ind +1:] #z obciętym elementem ind

        znak = (-1) ** (ind % 2)

        podmacierz = wyznacznik_macierzy(Ac)
        wynik += znak * podmacierz * A[0][ind]

    return wynik


A=[[-2,2,-3],[-1,5,3],[2,0,-1]]
print("Wyznacznik macierzy A: ",wyznacznik_macierzy(A))