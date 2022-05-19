

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


def detLU(A,n):

    s = 0
    for i in range(n):
        
        s = s + A[i][i]
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

#calcula o determinante da matriz A, de ordem n, decomposta por cholesky

def detCholesky(A,n):
    s = 0
    for i in range(n):
        s+= A[i][i]
    return s**2

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
            
            return [it, x, historico]

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
                
                print('A matriz A não é diagonal dominante. Insira uma matriz válida')
                return
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
        
        
        if (i) <= tol:
            
            return [it, x, historico]
        else:
            
            it+=1
            
            

           


M = []
with open('mat.dat','r') as arq:
    
    for linha in arq:
        a = []
        for i in linha.split():
            a.append(float(i))
        M.append(a)


x = []


with open('input.txt','r') as arquivo:
    L = []
    for i in arquivo:
        L.append(i)
    N = int(L[0])
    ICOD = int(L[1])
    IDET = int(L[2])
    tol = float(L[3].split()[0])
    if L[4] == 's':
        
        with open('chute.dat') as ch:
            for i in ch:
                x.append(float(i))


        

if (ICOD not in [1,2,3,4]) or (IDET not in [0,1]):
    with open('output.txt','w') as out:
        out.write('arquivo inválido. vise-o e tente novamente')
        
    input()
    exit()


if IDET == 1 and ICOD not in [1,2]:
    with open('output.txt','w') as out:
        out.write('não é possível calcular determinante. arrume o arquivo e tente novamente')
        
    input()
    exit()

#executa os métodos
        
if ICOD == 1:
    
    if IDET == 1:
        D = detLU(M,N)        
        with open('output.txt','w') as out:
            out.write('DETERMINANTE: '+ str(D) + '\n\n\n')
            M = sistLU(M,V,N)
            for elem in M:
                out.write(str(elem)+'\n')
    else:               
        with open('output.txt','w') as out:

            
            M = sistLU(M,V,N)
            for elem in M:
                out.write(str(elem)+'\n')
            
    
    

        

elif ICOD == 2:

    if IDET == 1:
        with open('DET.txt','w') as det:
            det.write('DETERMINANTE:  '+str(D))
        D = detCholesky(M,N)
        M = sistCholesky(M,V,N)
        with open('output.txt','w') as out:
            for elem in M:
                out.write(str(elem)+'\n')
            
        
    else:
            
        M = sistCholesky(M,V,N)
        with open('output.txt','w') as out:
            for elem in M:
                out.write(str(elem)+'\n')
           
    
            
elif ICOD == 3:#[it, x, historico]
    
    M = Jacobi(M, V, N, x, tol)

    if type(M)==str:
       with open('output.txt','w') as out:
           out.write((M))
    else:
        with open('output.txt','w') as out:
            for elem in M[1]:
                out.write(str(elem)+'\n')
            out.write('Nº de iterações: '+str(M[0]))
            out.write('\nhistórico: '+str(M[2]))

else:
    M = GaussSeidel(M, V, N, x, tol)
    if type(M)==str:
       with open('output.txt','w') as out:
           out.write((M))
    else:
        with open('output.txt','w') as out:
            for elem in M[1]:
                out.write(str(elem)+'n')
            out.write('Nº de iterações: '+str(M[0]))
            out.write('histórico: '+str(M[2]))
    


input()

exit()
    

