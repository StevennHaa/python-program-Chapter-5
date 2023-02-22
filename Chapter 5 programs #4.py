#4
from math import*
def main():
    y=pi
    radius=[2,5,6]
    for x in range (3):
        area=y*radius[x]**2
        print("{0:<10s}{1:<5.1f}{2:<5}{3:<10.1f}".format("The area of a circle with the radius of", radius[x],"is", area))
main()