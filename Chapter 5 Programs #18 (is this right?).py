#18
from math import*
def main():
    angle=eval(input("Enter the angle of the triangle"))
    atr= radians(angle)
    print("Your angle in radians is", atr)
    s=sin(atr)
    print("The sine of this angle is", s)
    c=cos(atr)
    print("The cosine of this angle is",c)
    t=tan(atr)
    print("The tangent of this angle is",t)
main()


