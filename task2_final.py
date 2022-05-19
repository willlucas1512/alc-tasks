from math import pi
from math import atan
from math import sin
from math import cos
import numpy as np


#calcula um auto valor e seu correspondente auto vetor pelo metodo das potencias




def Potencia(A,v,n):
    if len(v) == 0:
        for i in range(n):
            v.append(1.0)
    
    
    L0 = 1
    it = 1
    k = True
    while k:
        x0 = []
        for i in v:
            x0.append(i)
        
        
        for i in range(n):#multiplicando matriz por vetor (Ax)
            s=0
            for j in range(n):
                s+= A[i][j]*x0[j]
            
            v[i] = s
       
        L = v[0]#atribuindo proximo autovalor
        
        for i in range(n):#fatorando X
            v[i]= v[i]/L
        if (abs(L - L0)/abs(L)) <= tol:
            k = False
            return [L, v, it]
        else:
            L0 = L
            it+= 1

#-------------------------------------------------------------------

#cria uma matriz identidade de ordem n

            
def Identidade(n):
    A=[]
    for i in range(n):
        B=[]
        for j in range(n):
            if i == j:
                B.append(1)
            else:
                B.append(0)

        A.append(B)
    return A


#-------------------------------------------------------------------


#multiplica matriz A por B


def MultMatriz(A,B):
    
    if len(A[0]) != len(B):
        print('matrizes incompativeis')
        return
            
    M=[]
    
    for L in A:
        linha = []
        i = 0
        
        while i < len(L):
            s = 0
            j = 0
            
            while j < len(B):
                s+= L[j] * B[j][i]
                j+=1
            i+=1
            linha.append(round(s,5))
        M.append(linha)
        
    
        
    return M

#-------------------------------------------------------------------





#retorna a transposta da matriz A

def Transposta(A):
    M = []
    j = 0
    while j < len(A[0]):
        
        linha = []
        i = 0
        while i < len(A):
            linha.append(A[i][j])
            i+=1
        j+=1
        M.append(linha)
    return M
            
#-------------------------------------------------------------------


#calcula auto valores e auto vetores de uma matriz A simetrica

def Jacobi(A,n,tol):

    

    
    
    x = Identidade(n)
    it = 1

    k = True

    i = 0
    while i < n:
        j = 0
        while j < n:
            if A[i][j] != A[j][i]:
                print('Matriz nao eh simetrica')
                return
            j+=1
        i+=1

    
    
    while True:
        
        
        c = abs(A[0][1])
        ind = [0,1]
        
        
        for i in range(n):  #procura maior valor absoluto fora da diag. principal
            for j in range(n):
                
                if (abs(A[i][j]) > c):
                    if (i != j) :
                    
                      
                        c = abs(A[i][j])
                        ind[0] = i
                        ind[1] = j
        
        p= ind[0]
        q= ind[1]
        if A[p][p]==A[q][q]:
            T = pi/4
        else:
            T = (atan(2*A[p][q]/(A[p][p] - A[q][q])))/2

        P = Identidade(n)
        
            
        P[p][p]=cos(T)
        P[p][q]=-sin(T)
        P[q][p]=sin(T)
        P[q][q]=cos(T)

        b = Transposta(P)
        A = np.dot(b, np.dot(A,P))
        # A = MultMatriz(Transposta(P), MultMatriz(A,P))
        x = np.dot(x,P)
        # x = MultMatriz(x, P)

        a = 0

        for i in range(n):
            for j in range(n):
                if i != j and abs(A[i][j]) < tol:
                    a+= 1
                
        if a == (n*(n-1)):
            
            return [it, A, x]
        else:
            it+= 1



#----------------------------------------------------------------------------------
            
            
def DetermJacobi(A,n):
    det = A[0][0]
    i=1
    while i<n:
        det*= A[i][i]
        i+=1
    return det

#-------------------------------------------------------------------

M = []
with open('mat_A_04.dat')as arq:
    for linha in arq:
        a = []
        for i in linha.split():
            a.append(float(i))
        M.append(a)

v = []

with open('input.txt') as arq:
    l=[]
    for i in arq:
        l.append(i)
    N = int(l[0])
    ICOD = int(l[1])
    IDET = int(l[2])
    tol = float(l[3])
    
    if l[4] == 's':
        with open('chute.dat') as ch:
            for i in ch:
                v.append(float(i))
    if IDET == 1 and ICOD != 2 or l[4] not in ['s','n']:
        with open('output.txt','w') as out:
            out.write('arquivo de input invalido. tente novamente')
            input()
            exit()
#pergunta ao usuario o que ele deseja


        

# if ICOD == 1:
#     print("seila")
#     M = Potencia(M, v, N)
#     with open('output.txt','w') as fora:
#         fora.write('autovalor encontrado: ' + str(M[0]) + '\n\n\n')
#         fora.write('numero de iteracoes: ' + str(M[2]) + '\n\n\n')
#         fora.write('auto vetor correspondente: \n\n\n')
#         for i in M[1]:
#             fora.write(str(i)+'\n')
        
        
    

# else:
M = Jacobi(M,N,tol)
# if IDET == 1:
print(M)
D = DetermJacobi(M[1],N)
with open('output_1.txt','w') as fora:      
    fora.write('Determinante: ' + str(D) + '\n\n\n\n')
    fora.write('MATRIZ DOS AUTOVALORES: \n\n\n\n')
    for i in M[1]:
        for j in i:
            fora.write(str(j) +' ')
        fora.write('\n')
with open('outpu_2.txt','w') as fora:
    fora.write('MATRIZ DOS AUTOVETORES \n\n\n\n')
    for i in M[2]:
        for j in i:
            fora.write(str(j)+' ')
        fora.write('\n')
            
    # else:
    #     with open('output_1.txt','w') as fora:
        
    #         fora.write('MATRIZ DOS AUTOVALORES: \n\n\n\n')
    #         for i in M[1]:
    #             for j in i:
    #                 fora.write(str(j) +' ')
    #             fora.write('\n')
    #     with open('outpu_2.txt','w') as fora:
    #         fora.write('MATRIZ DOS AUTOVETORES \n\n\n\n')
    #         for i in M[2]:
    #             for j in i:
    #                 fora.write(str(j)+' ')
    #             fora.write('\n')



