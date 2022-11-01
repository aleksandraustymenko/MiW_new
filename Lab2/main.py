def zamien_rzad(Am, i, j):
    Am[i], Am[j] = Am[j], Am[i]
    return A


def transformacja(Am, x, i, j):
    for a in range(len(Am[i])):
        Am[j][a] = Am[j][a] + (x * Am[i][a])
    return Am


def macierz(Am):
    rzad = min(len(Am[0]), len(Am))

    i = 0
    while (i < rzad):
        if Am[i][i] != 0:
            j = 0
            while (j < len(Am)):
                if (i != j):
                    x = (Am[j][i] / Am[i][i]) * (-1)
                    m = 0
                    while (m < rzad - 1):
                        Am = transformacja(Am, x, m, j)
                        m += 1
                    Am[j][i] = 0
                j += 1
        else:
            temp = 0
            k = i + 1
            while (k < rzad):
                if Am[k][i]:
                    zamien_rzad(Am, i, k)
                    temp = 1
                    break
                k += 1
            if temp == 0:
                num = 1

                for y in range(i + 1, rzad):
                    if (Am[y][i] != 0):
                        num = 0
                        break
                if num == 1:
                    for k in range(len(Am)):
                        Am[k][i], Am[k][len(Am[0]) - 1] = Am[k][len(Am[0]) - 1], Am[k][i]
                    rzad -= 1
            i -= 1
        i += 1
    return rzad

A = [[1,2,3],[3,6,7],[8,6,8]]
print("Rząd macierzy wynosi:", macierz(A))

