import numpy

def main():
    ## correct answer:2.5365259511824627
    A=numpy.array([[1,1,0.5],[1,1,0.25],[0.5,0.25,2]])
    lamb=power_interation(A,1e-7,A.shape[0])
    print(f'{lamb}')
    
def power_interation(A,epsilon,n):
    V0=numpy.ones((n,1))
    V_old=V0.copy()
    m_old=numpy.max(abs(V_old))
    while True:
       u_old=V_old/m_old
       V_new=numpy.dot(A,u_old)
       m_new=numpy.max(abs(V_new))
       if abs(m_old-m_new)<epsilon:
           break
       m_old=m_new
       V_old=V_new
    return m_new
    

if __name__ == "__main__":
    main()