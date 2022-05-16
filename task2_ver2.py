
from math import pi
from math import atan
from math import sin
from math import cos

def Potencia(A,v,tol=10**(-3)):
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




'''
A = [[1,4,2,6,2],
     [4,78,3,1,7],
     [3,7,5,8,0],
     [1,2,3,4,5],
     [2,7,5,9,0]]
     
B = [[1,2,6,3,8],
     [3,4,2,6,2],
     [2,7,4,5,7],
     [1,4,1,2,3],
     [1,3,1,2,2]]

MultMatriz(A,B)
'''

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
            



def Jacobi(A,n,tol=10**(-2),IDET = 0):
    
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

                
            if IDET > 0:
                det = A[0][0]
                i=1
                while i<n:
                    det*= A[i][i]
                print(det)
            
            
            return it
        else:
            it+= 1
        

A = [[1,.2,0],
     [.2,1,.5],
     [0,.5,1]]

print(Jacobi(A,3))


    


















