import math
## calculate the integral of exp(x^2)


def main():
    eps=1e-7
    b=2
    a=1
    hmax=math.pow(eps/(16*b**4+48*b**2+12)/math.exp(b**2)*180/(b-a)*16,1/4)
    nmin=math.ceil((b-a)/hmax)
    result=composite_Simpson(f,a,b,nmin)
    print(result)
    
def composite_Simpson(f, a, b,n):
    sum=0
    h=(b-a)/n
    for i in range(0,n):
        sum+=(f(a+i*h)+4*f(a+(i+0.5)*h)+f(a+(i+1)*h))
    return sum*h/6
    
def f(x):
    return math.exp(x**2)
    
if __name__ == "__main__":
    main() 