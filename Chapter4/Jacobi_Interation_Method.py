import numpy
import math

def main():
    ## only for symmetric matrix
    A=numpy.array([[2,-1,0],[-1,2,-1],[0,-1,2]],dtype=numpy.float64)
    A,mT=jacobi_interation(A,1e-3,A.shape[0])
    print(A,mT)
    
def jacobi_interation(A,epsilon,n):
    maxrow,maxcol=1,0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if abs(A[i][j])>abs(A[maxrow][maxcol]):
                maxrow,maxcol=i,j
    c,s,JT=crate_rotate(n,maxrow,maxcol,A[maxrow][maxcol],A[maxcol][maxcol],A[maxrow][maxrow])
    mT=numpy.eye(n)
    while True:
        p,q=maxrow,maxcol
        mT=numpy.dot(JT,mT)
        Apq=A[p][q]
        Aqq=A[q][q]
        App=A[p][p]
        for i in range(n):
            if i!=q and i!=p:
                temp1,temp2=A[p][i],A[q][i]
                A[i][p]=c*temp1-s*temp2
                A[p][i]=c*temp1-s*temp2
                if abs(A[i][p])>abs(A[maxrow][maxcol]):
                    maxrow=min(p,i)
                    maxcol=max(p,i)
                A[i][q]=s*temp1+c*temp2
                A[q][i]=s*temp1+c*temp2
                if abs(A[i][q])>abs(A[maxrow][maxcol]):
                    maxrow=min(q,i)
                    maxcol=max(q,i)
        A[p][q],A[q][p]=0,0
        A[p][p]=c*c*App-2*s*c*Apq+s*s*Aqq
        A[q][q]=s*s*App+2*s*c*Apq+c*c*Aqq
        if abs(off_diagonal(A,n))<epsilon:
            break
        c,s,JT=crate_rotate(n,maxrow,maxcol,A[maxrow][maxcol],A[maxcol][maxcol],A[maxrow][maxrow])
    return A,mT
    
def off_diagonal(A,n):
    sum=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                sum+=abs(A[i,j])
    return sum

def crate_rotate(n,p,q,Apq,Aqq,App):
    J=numpy.eye(n)
    if App==Aqq:
        phi=math.pi/4
    else:
        phi=math.atan(2*Apq/(Aqq-App))/2
    J[p][p],J[q][q]=math.cos(phi),math.cos(phi)
    J[p][q],J[q][p]=math.sin(phi),-math.sin(phi)
    return math.cos(phi),math.sin(phi),numpy.transpose(J)

    
if __name__ == "__main__":
    main()