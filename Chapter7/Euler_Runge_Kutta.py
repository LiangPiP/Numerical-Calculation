import numpy

# solve the ODE: dy/dx=x-y^2+1, x(0)=0,y(0)=1


def main():
    x0=0
    y0=0
    y_old=y0
    h=0.1
    E,R=numpy.array([]),numpy.array([])
    for i in range(10):
        y_new=Euler(x0,y_old,h)
        E=numpy.append(E,y_new)
        y_old=y_new
    y_old=y0
    for i in range(10):
        y_new=Runge_Kutta(x0,y_old,h)
        R=numpy.append(R,y_new)
        y_old=y_new
    print(E)
    print(R)
    
def Euler(x,y,h):
    return y+h*f(x,y)

# 4 order Runge-Kutta method    
def Runge_Kutta(x,y,h):
    K1=f(x,y)
    K2=f(x+h/2,y+h/2*K1)
    K3=f(x+h/2,y+h/2*K2)
    K4=f(x+h,y+h*K3)
    return y+h/6*(K1+2*K2+2*K3+K4)
    
def f(x,y):
    return x-y*2+1
        
if __name__ == "__main__":
    main() 

