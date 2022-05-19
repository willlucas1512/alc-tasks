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
                # e**(1/x)
                print(listapontos[i][0])
                matrizP[i].append(math.e**1/listapontos[i][0])
            else:
                # sqrt(x)
                matrizP[i].append(math.sqrt(listapontos[i][0]))
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
        for j in range(0, 2):
            listapontos[i].append(float(linhas[int(i)][int(j)]))  
        if i < paresN - 1:
            listapontos.append(list())

    return listapontos


with open('input_task3.txt') as file:  
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

icod = int(lines[0])
paresN = int(lines[1])
x = float(lines[2])

linhas=[]
with open('pointsb.dat') as file:
    for linha in file:
        linhas.append(linha.split())
    # linhas = file.readlines()
    # linhas = [linha.strip() for linha in linhas]

listapontos = coordenadas(linhas, paresN)

if icod == 1:
    saida = interpolacao(x, listapontos, paresN)
elif icod == 2:
    saida = regressao(x, listapontos, paresN)

with open('output_regressao.txt', 'a') as the_file:
    the_file.write('y = ' + saida)