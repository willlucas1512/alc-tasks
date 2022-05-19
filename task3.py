import numpy as np
import math

def interpolacao(x, listapontos, paresN):
    phi = 1
    y = 0
    for i in range(0, paresN):
        for j in range(0, paresN):
           if j != i:
               phi *= (x - listapontos[j][0]) / (listapontos[i][0] - listapontos[j][0])
        y += phi * listapontos[i][1]
        phi = 1
    return str(y)

def regressao(x, listapontos, paresN):
    # matriz dos regressores
    matrizP = [[]]
    matrizY = []
    for i in range(0, paresN):
        for j in range(0, 2):
            if j == 0:
                # 1/e^x
                matrizP[i].append(1/math.pow(math.e, listapontos[i][0]))
            else:
                # ln(x)
                matrizP[i].append(math.log(listapontos[i][0], math.e))
        matrizY.append(listapontos[i][1])
        if i < paresN - 1:
            matrizP.append(list())
    # matriz P transposta        
    matrizPt = np.transpose(matrizP)
    # A = Pt * P
    matrizA = np.dot(matrizPt, matrizP)
    # C = Pt * Y
    matrizC = np.dot(matrizPt, matrizY)
    # A inversa
    MatrizAinv = np.linalg.inv(matrizA)
    # B = A inversa * C
    matrizB = np.dot(MatrizAinv, matrizC)
    # y = b1 * 1/e^x + b2 * ln(x)
    y = (matrizB[0] / math.e ** x) + matrizB[1] * math.log(x, math.e)
    return str(y)

def coordenadas(linhas, paresN):
    listapontos = [[]]

    for i in range(0, paresN):
        for j in range(0, 3):
            if j != 1:
                listapontos[i].append(int(linhas[int(i)][int(j)]))  
        if i < paresN - 1:
            listapontos.append(list())

    return listapontos


with open('input_task3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

icod = int(lines[0])
paresN = int(lines[1])
x = int(lines[2])

with open('pontos_task3.dat') as file:
    linhas = file.readlines()
    linhas = [linha.rstrip() for linha in linhas]

listapontos = coordenadas(linhas, paresN)

if icod == 1:
    saida = interpolacao(x, listapontos, paresN)
elif icod == 2:
    saida = regressao(x, listapontos, paresN)

with open('output_task3.txt', 'a') as the_file:
    the_file.write('y = ' + saida)