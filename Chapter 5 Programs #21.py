#21
from random import randrange
def main():
    count2=0
    count3=0
    count4=0
    count5=0
    for x in range(25):
        r=randrange(5,101)
        dt=r%2
        dtr=r%3
        df=r%4
        dfiv=r%5
        print(r)
        if dt==0:
            count2=count2+1
            print(count2,"is how many numbers are divisible by 2")
        if dtr==0:
            count3=count3+1
            print(count3,"is how many numbers are divisible by 3")
        if df==0:
            count4=count4+1
            print(count4,"is how many numbers are divisible by 4")
        if dfiv==0:
            count5=count5+1
            print(count5,"is how many numbers are divisible by 5")
main()