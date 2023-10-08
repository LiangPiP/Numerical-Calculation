import math
import numpy

def main():
    eps=1e-7
    b=2
    a=1
    n=2
    T,S,C,R=numpy.array([composite_Trapezoidal(f,a,b,n)]),numpy.array([]),numpy.array([]),numpy.array([])
    while True:
        n*=2
        T=numpy.append(T,composite_Trapezoidal(f,a,b,n))
        if len(T)>1:
            S=numpy.append(S,(4*T[-1]-T[-2])/3)
        if len(S)>1:
            C=numpy.append(C,(16*S[-1]-S[-2])/15)
        if len(C)>1:
            R=numpy.append(R,(64*C[-1]-C[-2])/63)
        if len(R)>1 and abs(R[-1]-R[-2])<eps:
            break

    print(f"Romberg Integration: {R[-1]}")
    
def composite_Trapezoidal(f, a, b , n):
    sum=0
    h=(b-a)/n
    for i in range(1,n):
        sum+=2*f(a+i*h)
    return (sum+f(a)+f(b))*h/2
    
def f(x):
    return math.exp(x**2)
    
if __name__ == "__main__":
    main()