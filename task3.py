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
    print('y = ' + str(y))
    return 0

def regressao(x, listapontos, paresN):
    matrizP = [[]]
    matrizY = []
    for i in range(0, paresN):
        for j in range(0, 2):
            if j == 0:
                matrizP[i].append(1/math.pow(math.e, listapontos[i][0]))
            else:
                matrizP[i].append(math.log(listapontos[i][0], math.e))
        matrizY.append(listapontos[i][1])

        if i < paresN - 1:
            matrizP.append(list())
    matrizPt = np.transpose(matrizP)
    matrizA = np.dot(matrizPt, matrizP)
    matrizC = np.dot(matrizPt, matrizY)
    MatrizAinv = np.linalg.inv(matrizA)
    matrizB = np.dot(MatrizAinv, matrizC)

    y = (matrizB[0] / math.e ** x) + matrizB[1] * math.log(x, math.e)
    print('y = ' + str(y))
    return 0


def pontox():
    while True:
        try:
            x = float(input('Deseja calcular o y de qual ponto x? '))
            break
        except ValueError:
                print('Favor inserir um numero (float).')
    return x

def coordenadas(paresN):
    listapontos = [[]]

    for i in range(0, paresN):
        for j in range(0, 2):
            try:
                if j == 0:
                    listapontos[i].append(float(input(str(i + 1) + 'a Coordenada: x = ')))
                else:
                    listapontos[i].append(float(input(str(i + 1) + 'a Coordenada: y = ')))
            except ValueError:
                print("Insira um float.")
                exit(0)
        if i < paresN - 1:
            listapontos.append(list())

    print('Lista de Coordenadas:')
    for i in range(len(listapontos)):
        print(listapontos[i])

    return listapontos


def paresN():
    while True:
        try:
            var_paresN = int(input('Qual eh o numero de pares de pontos (x,y)? '))
            if var_paresN < 1:
                print('Favor inserir um numero inteiro positivo e nao nulo.')
            else:
                break
        except ValueError:
                print('Favor inserir um numero inteiro.')
    return var_paresN


def icod():
    print('1 = Interpolacao\n2 = Regressao')
    while True:
        try:
            var_icod = int(input('Qual metodo sera utilizado? '))
            if var_icod != 1 and var_icod != 2:
                print('Favor inserir um valor valido para o metodo.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor valido para o metodo (1 ou 2)')
    return var_icod

var_paresN = paresN()
var_icod = icod()
x = pontox()
listapontos = coordenadas(var_paresN)

if var_icod == 1:
    interpolacao(x, listapontos, var_paresN)
elif var_icod == 2:
    regressao(x, listapontos, var_paresN)
