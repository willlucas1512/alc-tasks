#decompoe a matriz A de ordem n em uma matriz LU
def decompLU(A,n):
    j = 0
    while j<n:
        i = j+1
        while i < n:
            A[i][j] = A[i][j]/A[j][j]
            i+=1
        
        k = j+1
        while k < n:
            l = j+1
            while l < n:
                A[k][l] = A[k][l] - A[k][j] * A[j][l]
                l+=1
            k+=1
        j+=1
    return A

#resolve o sistema linear de ordem n Ax=B, usando decomposicao LU
def sistLU(A,B,n):
    A = decompLU(A,n)
    x = []
    i = 1
    x.append(B[0])
    while i < n:
        k = 0
        s = 0
        while k < i:
            s+= x[k] * A[i][k]
            k+=1
            
        x.append(B[i]-s)
        i += 1
    x[n-1] = x[n-1]/A[n-1][n-1]
    i = n-2
    while i >= 0:
        s = 0
        k = n-1
        while k > i:
            s += A[i][k] * x[k]
            k -= 1
        x[i] = (x[i] - s) / A[i][i]
        i -= 1
    return x


#calcula o determinante da matriz A decomposta em LU
def determLU(A,n):
    i = 0
    s = 0
    while i < n:
        s += A[i][i]
        i += 1
    return s


#faz a decomposicao de Cholesky na matriz A
def Cholesky(A,n):
    i = 1
    while i < n:
        j=0
        while j<i:
            if A[i][j] != A[j][i]:
                return "A nao eh simetrica, insira uma matriz valida"
            j+=1
        i+=1
        
    i = 0
    while i < n:
        k=0
        s=0
        while k<(i):
            s+= (A[i][k])**2
            k+=1
        if (A[i][i]-s) < 0:
            return "A nao eh semi-definida positiva, insira uma matriz valida"
        
        A[i][i] = ((A[i][i]-s)**(.5))
        
        j = i+1
        
        while j < n:
            l = 0
            s = 0
            
            while l<i:
                s+=A[i][l]*A[j][l]
                l+=1
            A[j][i]=((A[i][j]-s)/A[i][i])
            j+=1
        i+=1
    return A

# resolve o sistema pelo metodo de cholesky
def sistCholesky(A,B,n):
    A = Cholesky(A,n)
    x = []
    i = 1
    x.append(B[0]/A[0][0])
    while i < n:
        k = 0
        s = 0
        while k < i:
            s+= x[k] * A[i][k]
            k+=1
            
        x.append((B[i]-s)/A[i][i])
        i+=1
    print(x)
    x[n-1] = x[n-1]/A[n-1][n-1]
    i = n-2
    while i >= 0:
        s = 0
        k = n-1
        while k > i:
            s+= A[k][i] * x[k]
            k-= 1
        x[i] = (x[i] - s) / A[i][i]
        i-=1
    return x


#faz a norma euclidiana do vetor x de ordem n
def norma(x,n):
    i = 0
    s = 0
    while i < n:
        s += (x[i]**2)
        i +=1
    return ((s)**(.5))


#resolve o sistema pelo metodo de jacobi
def Jacobi(A,B,n,x,tol=(10**(-3))):
    it = 0
    historico = []
    while True:
        h = 0
        while h < n:
            j = h + 1
            s1 = 0
            s2 = 0
            while j<n:
                s1 += abs(A[h][j])
                s2 += abs(A[j][h])
                j += 1
            if (s1 or s2) > A[h][h]:
                return 'A matriz A nao eh diagonal dominante. Insira uma matriz valida'
            h += 1
        i = 0
        x0 = []
        h = 0
        while h < n:
            x0.append(x[h])
            h += 1
        while i < n:
            k = 0
            s = 0
            while k < n:
                 if k != i:
                     s+= A[i][k]*x0[k]
                     k+=1
                 else:
                        k+=1
            
            x[i] = ((B[i] - s)/A[i][i])
            i+=1
        l = 0
        for i in range(n):
            x0[i] -= x[i]
        if (norma(x0,n)/norma(x,n)) <= tol:            
            return it, x, historico
        else:
            it+=1
            historico.append(round((norma(x0,n)/norma(x,n)),4))

# resolve o sistema pelo metodo de gauss-seidel
def GaussSeidel(A,B,n,x,tol=(10**(-3))):
    it = 0
    historico = []
    while True:
        h=0
        while h<n:
            j=h+1
            s1=0
            s2=0
            while j<n:
                s1+=abs(A[h][j])
                s2+=abs(A[j][h])
                j+=1
            if (s1 or s2) > A[h][h]:
                return 'A matriz A nao eh diagonal dominante. Insira uma matriz valida'
            h += 1        

        i = 0
        x0 = []
        h = 0
        while h < n:
            x0.append(x[h])
            h += 1

        while i < n:
            k = 0
            s = 0
            while k < n:
                 if k != i:
                     s+= A[i][k]*x[k]
                     k+=1
                 else:
                        k+=1
            
            x[i] = ((B[i] - s)/A[i][i])
            i+=1
        l = 0
        
        for i in range(n):
            x0[i]-= x[i]

        if (norma(x0,n)/norma(x,n)) < tol:
            
            return it, x, historico
        else:
            it+=1
            historico.append(round((norma(x0,n)/norma(x,n)),3))
            

A=[[3,-1,-1],[-1,3,-1],[-1,-1,3]]
c=[1,1,1]
B=[1,2,1]
j = GaussSeidel(A,B,3,c)
d = Jacobi(A,B,3,c)
print("Utilizando o arquivo de entrada:")
method = int(input("Escolha o metodo de solucao: \n1 - Decomposicao LU \n3 - Decomposicao de Cholesky \n3 - Jacobi \n4 - Gauss-Seidel \n"))
calcdeterminant = int(input("Deseja calcular o determinante? \n1 - Sim \n2 - Nao \n"))
if method == 1:
    print("Decomposicao LU \n", sistLU(A,B,3))
    if calcdeterminant == 1:
        print("Determinante: ", determLU(A,3))
# elif method == '2':
#     print("Decomposicao de Cholesky \n", sistCholesky(A,B,3))
#     if calcdeterminant == '1':
#         print("Metodo iterativo. Nao e possivel calcular o determinante.")
# elif method == '3':
#     print("Jacobi \n", Jacobi(A,B,3,c))
#     if calcdeterminant == '1':
#          print("Metodo iterativo. Nao e possivel calcular o determinante.")
# elif method == '4':
#     print("Gauss-Seidel \n", GaussSeidel(A,B,3,c))
#     if calcdeterminant == '1':
#          print("Metodo iterativo. Nao e possivel calcular o determinante.")