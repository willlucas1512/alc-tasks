from math import pi
from math import atan
from math import sin
from math import cos


#calcula um auto valor e seu correspondente auto vetor pelo método das potências




def Potencia(A,v,n):
    L0 = 1
    it = 1
    while True:
        
        for i in range(n):
            s=0
            for j in range(n):
                s+= A[i][j]*v[j]
            v[i] = s
        
        L = v[0]
        for i in range(n):
            v[i]= v[i]/v[0]
        if ((abs(L - L0))/abs(L)) < tol:
            return L, v, it
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


#calcula auto valores e auto vetores de uma matriz A simétrica

def Jacobi(A,n,tol):

    

    
    
    x = Identidade(n)
    it = 1

    k = True

    i = 0
    while i < n:
        j = 0
        while j < n:
            if A[i][j] != A[j][i]:
                print('Matriz não é simétrica')
                return
            j+=1
        i+=1

    
    
    while True:
        
        
        c = abs(A[0][1])
        ind = [0,1]
        
        
        for i in range(n):
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

        

        A = MultMatriz(Transposta(P), MultMatriz(A,P))
        x = MultMatriz(x, P)

        a = 0

        for i in range(n):
            for j in range(n):
                if i != j and abs(A[i][j]) < tol:
                    a+= 1
                
        if a == (n*(n-1)):
            
            for i in A:
                print(i)
            for i in x:
                print(i)

                
            
                
            
            
            return it
        else:
            it+= 1



#----------------------------------------------------------------------------------
            
            
def DetermJacobi(A,n):
    det = A[0][0]
    i=1
    while i<n:
        det*= A[i][i]
    
    return det

#-------------------------------------------------------------------

M = []
arq = open('Matriz.dat')
for linha in arq:
    a = []
    for i in linha.split():
        a.append(float(i))
    M.append(a)
arq.close()

#pergunta ao usuário o que ele deseja
                 
k = True
while k:
    ICOD = input('insira ICOD')
    if ICOD not in ['1','2']:
        print('insira ICOD válido')
    else:
        ICOD = int(ICOD)
        k = False

        
k = True
while k:
    IDET = input('deseja calcular determinante? 0 se não, 1 se sim\n')
    if IDET not in ['0','1']:
        print('IDET inválido')
    else:
        IDET = int(IDET)
        k=False




if IDET == 1 and ICOD != 2:
    print('comando inválido, impossivel proceder')
    input('aperte qualquer tecla para fechar e abra novamente\n')
    exit()


#pergunta a ordem do sistema de equações

    
N = input('informe a ordem do sistema\n')
N = int(N)

#pergunta se o usuário quer usar uma tolerancia específica, ou a padrão(10^-3)

k = True
tol = 10**-3
while k:

    if ICOD == 2:
        tol = input('deseja especificar tolerancia? padrão = 10^-3 - s/n\n')
        if tol not in ['s','n']:
            print('resposta inválida')
        else:
            tol = float(input('valor:\n'))
            k = False





#pergunta se o usuário quer usar uma um vetor inicial específico, ou o padrão

k = True

x = []

while k:
    if ICOD == 2:
        x = input('deseja informar vetor inicial? padrão é vetor unitário - s/n\n')
        if x not in ['s','n']:
            print('insira resposta válida\n')
        else:
            x_=[]
            x = open('chute_inicial.dat')
            for i in x:
                x_.append(float(i))
            x = x_
            del x_
                
                
            k = False


if len(x)==0:
    for i in range(N):
        x.append(1)
        

if ICOD == 1:
    print(Potencia(M, x, N))

else:
    print(Jacobi(M, N, tol))

