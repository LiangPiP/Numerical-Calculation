import math

def main():
    init=float(input("init: "))
    epsilon=float(input("epsilon: "))
    x_old=init
    while True:
        x_new=x_old-f(x_old)/df(x_old)
        if abs(x_new-x_old)<epsilon:
            break
        x_old=x_new
    print(f"x={x_new}")
    
def f(x):
    return x-2*math.cos(x)

def df(x):
    return 1+2*math.sin(x)

if __name__ == "__main__":
    main()