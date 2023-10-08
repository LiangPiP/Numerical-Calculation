import math
## calculate the integral of exp(x^2)


def main():
    eps=1e-7
    b=2
    a=1
    hmax=math.sqrt(eps/(4*b**2+2)/math.exp(b**2)*12/(b-a))
    nmin=math.ceil((b-a)/hmax)
    result=composite_Trapezoidal(f,a,b,nmin)
    print(result)
    
def composite_Trapezoidal(f, a, b,n):
    sum=0
    h=(b-a)/n
    for i in range(1,n):
        sum+=2*f(a+i*h)
    return (sum+f(a)+f(b))*h/2
    
def f(x):
    return math.exp(x**2)
    
if __name__ == "__main__":
    main()