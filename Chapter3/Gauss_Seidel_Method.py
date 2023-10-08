import numpy

def main():
    A=numpy.array([[5,2,3],[1,4,2],[2,-3,10]])
    b=numpy.array([-12,20,3]).reshape(3,1)
    x=Guass_Seidel(A,b,epsilon=1e-7)
    print(f"{x}")

def Guass_Seidel(A,b,epsilon=1e-3):
    n=A.shape[0]
    x=numpy.zeros((n,1))
    while True:
        x_old=x.copy() ## attention, x_old=x will not work
        for i in range(n):
            temp=0
            for j in range(n):
                if j!=i:
                    temp+=A[i][j]*x[j]
            x[i]=(b[i]-temp)/A[i][i]
        sum=0
        for i in range(n):
            sum+=(x[i]-x_old[i])**2
        if sum<epsilon**2:
            break
    return x
    
if __name__ == "__main__":
    main()
    

 
    
    