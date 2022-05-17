

#decompõe a matriz A de orndem n em uma matriz LU

def decompLU(A,n):
    j = 0
    while j < n:
        i = j+1
        while i < n:
            A[i][j] = round((A[i][j] / A[j][j]), 4)
            p = j+1
            while p < n:
                A[i][p] = round((A[i][p] -(A[i][j] * A[j][p])),4)
                p+= 1
            i+= 1
        j+=1
        
    return A
    
        



#resolve o sistema linear de ordem n Ax=B, usando decomposição LU

def sistLU(A,B,n):
    
    A = decompLU(A,n)
    
    i = 1
    
    while i < n:
        k = 0
        s = 0
        while k < i:
            s+= B[k] * A[i][k]
            k+=1
            
        B[i] = B[i]-s
        i+=1
    B[n-1] = B[n-1]/A[n-1][n-1]
    i = n-2
    while i >= 0:
        s = 0
        k = n-1
        while k > i:
            s+= A[i][k] * B[k]
            k-= 1
        B[i] = (B[i] - s) / A[i][i]
        i-=1
    return B



#calcula o determinante da matriz A decomposta em LU


def determLU(A,n):

    s = 0
    for i in range(n):
        
        s+= A[i][i]
    return s




#faz a decomposição de Cholesky na matriz A

def Cholesky(A,n):
    i = 1
    
    while i < n:
        j=0
        
        while j<i:
            
            if A[i][j] != A[j][i]:
                return "A não é simétrica, insira uma matriz válida"
            j+=1
        i+=1
        
    i = 0
    
    while i < n:
        k=0
        s=0
        
        while k < i:
            s+= (A[i][k])**2
            k+=1
            
        if (A[i][i]-s) <= 0:
            print("A não é semi-definida positiva, insira uma matriz válida")
            return
        
        A[i][i] = ((A[i][i]-s)**(.5))
        
        
        j = i+1
        
        while j < n:
            l = 0
            s = 0
            
            while l < i:
                s+=A[i][l]*A[j][l]
                l+=1
            A[j][i]=((A[i][j]-s)/A[i][i])
            j+=1
        i+=1
        
        
    return A


#Resolve o sistem Ax=B, sendo A uma matriz que sofreu a decomposição de Cholesky


def sistCholesky(A,B,n):

    A = Cholesky(A,n)
    
    i = 1
    B[0] = B[0]/A[0][0]
    while i < n:
        k = 0
        s = 0
        while k < i:
            s+= B[k] * A[i][k]
            k+=1
            
        B[i] = (B[i]-s)/A[i][i]
        i+=1
    print(B)
    B[n-1] = B[n-1]/A[n-1][n-1]
    i = n-2
    while i >= 0:
        s = 0
        k = n-1
        while k > i:
            s+= A[i][k] * B[k]
            k-= 1
        B[i] = (B[i] - s) / A[i][i]
        i-=1
    print(B)
    return B
'''
B = [.6,-.3,-.6]
sistCholesky(A, B, 3)
'''
#faz a norma euclidiana do vetor x 


def norma(x):
    
    s=0
    for i in range(len(x)):
        s+= (x[i]**2)
        
    return ((s)**(.5))




#resolve o sistema pelo metodo de jacobi




def Jacobi(A, B, n, x, tol):
    
    

    it = 1
    historico = []
    while True:
        
    
    
        i = 0
        while i < n:
            j = 0
            s1=0
            s2=0
            while j < n:
                if i != j:
                    s1+= abs(A[i][j])
                    s2+= abs(A[j][i])
                    j+=1
                    
                else:
                    j+=1
                    
            if (s1 or s2) > A[i][i]:
                return 'A matriz A não é diagonal dominante. Insira uma matriz válida'
                    
            i+=1
        
        
        x0 = []
        
        for i in x:
            x0.append(i)
        
            
        
        i = 0
        while i < n:
            
            j = 0
            s = 0
            while j < n:
                 if j != i:
                     s+= A[i][j]*x0[j]
                     j+=1
                 else:
                        j+=1
            
            x[i] = round(((B[i] - s)/A[i][i]),5)
        
            i+=1
        
        
        
        for i in range(n):
            x0[i]-= x[i]

        i = norma(x0)/norma(x)
        
        
        historico.append(round(i,4))
        
        
        if (norma(x0)/norma(x)) <= tol:            
            
            return it, x, historico

        else:
            it+=1

            historico.append(round((norma(x0)/norma(x)),5))


#Resolve o sistema Ax=B pelo método iterativo de GaussSeidel



def GaussSeidel(A,B,n,x,tol):
    


    it = 1
    historico = []
    while True:
        
        i=0
        while i < n:
            
            j=i+1
            s1=0
            s2=0
            while j < n:
                
                if i != j:
                    
                    s1+=abs(A[i][j])
                    s2+=abs(A[j][i])
                    j+=1
                else:
                    
                    j+=1
            if (s1 or s2) > A[i][i]:
                
                return 'A matriz A não é diagonal dominante. Insira uma matriz válida'
            i+=1        

        
        
        x0 = []
        
        for i in x:
            
            x0.append(i)
            
        i = 0
        
        
        while i < n:
            
            j = 0
            s = 0
            while j < n:
                
                if j != i:
                     
                     s+= A[i][j]*x[j]
                     j+=1
                else:
                     
                    j+=1
            
            x[i] = round(((B[i] - s)/A[i][i]),5)
            i+=1
        
        
        for i in range(n):
            
            x0[i]-= x[i]
        
        i = norma(x0)/norma(x)
        historico.append(round(i,3))
        print(x, i, it)
        
        if (i) <= tol:
            
            return it, x, historico
        else:
            
            it+=1
            
            


#coleta a matriz e salva na variavel M, e o vetor e o salva na variável V
#precisam ser arquivos diferentes
#a matriz deve ter suas linhas separadas pelas linhas do arquivo, e os elementos separados por espaço            


M = []
arq = open('Matriz.dat')
for linha in arq:
    a = []
    for i in linha.split():
        a.append(float(i))
    M.append(a)
arq.close()
V = []
arq = open('vetor.dat')
for i in arq.split():
    V.append(float(i))
arq.close()



#pergunta ao usuário o que ele deseja
                 
k = True
while k:
    ICOD = input('insira ICOD')
    if ICOD not in ['1','2','3','4']:
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




if IDET == 1 and ICOD != 1:
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

    if ICOD == (3 or 4):
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
    if ICOD == (3 or 4):
        x = input('deseja informar vetor inicial? padrão é vetor unitário - s/n\n')
        if x not in ['s','n']:
            print('insira resposta válida\n')
        else:
            x = open('chute_inicial.dat')
            k = False


#executa os métodos
        
if ICOD == 1:
    print(sistLU(M,V,N))
    if IDET == 1:
        print(determLU(M,N))

elif ICOD == 2:
    print(sistCholesky(M,V,N))

elif ICOD == 3:
    print(Jacobi(M, V, N, x, tol))

else:
    print(GaussSeidel(M, V, N, x, tol))


input()

exit()
    


            
            
        
    
    







    






        
        
    

















