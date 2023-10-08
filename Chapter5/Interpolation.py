import numpy 

def lagrange(x,y,s):
    n=x.shape[0]
    sum=0
    for i in range(n):
        for j in range(n):
            factor=1
            if i!=j:
                factor*=(s-x[j])/(x[i]-x[j])
        sum+=y[i]*factor
    return sum

def Newton(x,y,s):
    n=x.shape[0]
    sum=0
    mat=numpy.zeros((n,n))
    mat[:][0]=y.reshape((n,1))
    for i in range(1,n):
        for j in range(0,n-i):
            mat[j][i]=(mat[j][i-1]-mat[j+1][i-1])/(x[j]-x[j+i])
    for i in range(n):
        factor=1
        for j in range(i):
            factor*=(s-x[j])
        sum+=mat[0][i]*factor
    return sum