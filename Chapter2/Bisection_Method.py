import math
import argparse

def main():
    args=get_input()
    l,r,epsilon=args.l,args.r,args.e
    while True:
        m=(l+r)/2
        if abs(f(m))<epsilon:
            break
        if f(l)*f(m)<0:
            r=m
        else:
            l=m
    print(f"x={m}")
    
def f(x):
    return x-2*math.cos(x)

def df(x):
    return 1+2*math.sin(x)

def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l",type=float,help="left boundary")
    parser.add_argument("-r",type=float,help="right boundary")
    parser.add_argument("-e",type=float,help="epsilon")
    input_eval(parser.parse_args().l,parser.parse_args().r)
    return parser.parse_args()

def input_eval(a,b):
    if f(a)*f(b)>=0:
        exit("f(a) and f(b) must have different signs")
    if a>=b:
        exit("b must be greater than a")


if __name__ == "__main__":
    main()