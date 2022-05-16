

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
        '''
    for i in range(n):
        print(A[i])
        '''
    return A
    
        
'''         

#A = [[1,2,2],[4,4,2],[4,6,4]]
A = [[47,95,37,88,23],
[80,28,14,80,85],
[47,37,14,52,50],
[81,70,80,52,48],
[17,38,50,15,59]]
decompLU(A,5)

'''


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

#A = [[1,2,2],[4,4,2],[4,6,4]]
#B = [3,6,10]
#A = [[1,1,1,0],[1,0,1,1],[0,1,1,1],[1,1,0,1]]
#B = [-1,5,7,4]
#A = [[2,-1,4,1,-1],
#     [-1,3,-2,-1,2],
#     [5,1,3,-4,1],
#     [3,-2,-2,-2,3],
#     [-4,-1,-5,3,-4]]
#B = [7,1,33,24,-49]
#print(sistLU(A, B, 5))

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
        '''
    for a in range(n):
        print(A[a])
        '''
        
    return A
'''
A = [[1,.2,.4],[.2,1,.5],[.4,.5,1]]

A = [[1,5,-3,9],
     [5,0,2,-1],
     [-3,2,8,4],
     [9,-1,4,6]]

Cholesky(A,3)

'''
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




def Jacobi(A,B,n,x = None,tol=(10**(-3))):
    if x == None:
        x = []
        for i in range(n):
            x.append(1)
    

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
            
            x[i] = round(((B[i] - s)/A[i][i]),3)
        
            i+=1
        
        
        
        for i in range(n):
            x0[i]-= x[i]

        i = norma(x0)/norma(x)
        
        #print(x, i, it)
        historico.append(round(i,4))
        
        
        if (norma(x0)/norma(x)) <= tol:            
            
            return it, x, historico

        else:
            it+=1

            historico.append(round((norma(x0)/norma(x)),4))
'''
A = [[3,-1,-1],[-1,3,-1],[-1,-1,3]]
B = [1,2,1]
print(Jacobi(A, B, 3))
'''





def GaussSeidel(A,B,n,x=[],tol=(10**(-3))):
    if len(x) == 0:
        for i in range(n):
            x.append(1)


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
            
            x[i] = round(((B[i] - s)/A[i][i]),3)
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
            
            

A=[[3,-1,-1],[-1,3,-1],[-1,-1,3]]
B=[1,2,1]
print(GaussSeidel(A,B,3))



#d=Jacobi(A,B,3,c)













    






        
        
    

















