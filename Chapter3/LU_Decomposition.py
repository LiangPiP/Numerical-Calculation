import numpy
from scipy.linalg import lu


def main():
    A=numpy.array([[5,2,3],[1,4,2],[2,-3,10]])
    b=numpy.array([-12,20,3]).reshape(3,1)
    n=b.shape[0]
    x=solver(*Doolittle_decompose(A,n),b,n)
    print(f"{x}")

def Doolittle_decompose(A,n):
    L,U=numpy.zeros((n,n)),numpy.zeros((n,n))
    U[0][:]=A[0][:].copy()    
    for i in range(n):
        L[i][i]=1
        if i>0:
            L[i][0]=A[i][0]/A[0][0]
            
    for i in range(1,n):
         for j in range(i,n):
            U[i][j]=A[i][j]
            for k in range(0,i):
                U[i][j]-=L[i][k]*U[k][j]
         for j in range(i+1,n):
             L[j][i]=A[j][i]
             for k in range(0,i):
                L[j][i]-=L[j][k]*U[k][i]
             L[j][i]/=U[i][i]
                  
    print(L,U)
    return L,U

## Ax=LUx=b, Ux=y, Ly=b
def solver(L,U,b,n):
    y=L_solver(L,b,n)
    x=U_solver(U,y,n)
    return x

def L_solver(L,b,n):
    x=numpy.zeros((n,1))
    for i in range(n):
        x[i]=b[i]
        for j in range(0,i):
            x[i]-=x[j]*L[i][j]
    return x

def U_solver(U,b,n):
    x=numpy.zeros((n,1))
    for i in range(n):
        x[n-i-1]=b[n-i-1]
        for j in range(n-i,n):
            x[n-i-1]-=x[j]*U[n-i-1][j]
        x[n-i-1]/=U[n-i-1][n-i-1]
    return x

if __name__ == "__main__":
    main()