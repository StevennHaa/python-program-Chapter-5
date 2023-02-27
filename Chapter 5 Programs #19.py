#19
from random import randrange
def main():
    sum=0
    r=11
    while r!=0:
        r= randrange(0,10)
        print(r)
        sum=sum+r
    print("The sum is", sum)
main()