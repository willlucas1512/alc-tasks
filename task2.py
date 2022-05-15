from math import pi
from math import atan
from math import sin
from math import cos

def Potencia(A,v,tol=10**(-3)):
    L0 = 1
    it = 0
    while True:
        
        for i in range(n):
            s=0
            for j in range(n):
                s+= A[i][j]*v[j]
            v[i]=s
        
        L=v[0]
        for i in range(n):
            v[i]= v[i]/v[0]
        if ((abs(L - L0))/abs(L)) < tol:
            return L, v, it
        else:
            L0 = L
            it+=1


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
    n=range(len(A))
    for i in n:
        s = 0
        for j in n:
            s+=A[i][j]*B[j][i]
        A[



def Jacobi(A,n,tol=10**(-2)):
    x0= Identidade(n)
    while True:
        k=0
        
        c = abs(A[0][0])
        ind = [0,0]
        
        for i in range(n):
            for j in range(n):
                
                if abs(A[i][j]) > c:
                    
                    c= abs(A[i][j])
                    ind[0]=i
                    ind[1]=j
                else:
        m= ind[0]
        n= ind[1]
        if A[m][m]==A[n][n]:
            T = pi/4
        else:
            T = (atan((2*A[m][m])/(A[n][n]-A[m][m])))
        x0[m][m]=cos(T)
        x0[m][n]=-sin(T)
        x0[n][m]=sin(T)
        x0[n][n]=cos(T)

