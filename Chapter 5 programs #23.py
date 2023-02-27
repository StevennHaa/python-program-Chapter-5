#23
from random import randrange
def main():
    print("{0:<10}{1:<10}{2:<10}".format("Horse 1", "Horse 2", "Horse 3"))
    horse1=0
    horse2=0
    horse3=0
    while horse1<50 and horse2<50 and horse3<50:
        r1=randrange(2,7)
        r2=randrange(2,7)
        r3=randrange(2,7)
        horse1=horse1+r1
        horse2=horse2+r3
        horse3=horse3+r3
        print("{0:<10}{1:<10}{2:<10}".format(horse1, horse2, horse3))
    if horse1==horse2 and horse2==horse3 and horse1==horse3:
        print("Tie")
    if horse1>=50 and horse1>horse2 and horse1>horse3:
        print("Horse 1 wins")
    if horse2>=50 and horse2>horse1 and horse2>horse3:
        print("Horse 2 wins")
    if horse3>=50 and horse3>horse1 and horse3>horse2:
        print("Horse 3 wins")
    if horse1>=50 and horse2>=50 and horse1==horse2 and horse3<horse2 and horse1>horse3:
        print("It's a tie")
    if horse1>=50 and horse3>=50 and horse1==horse3 and horse2<horse3 and horse2<horse1:
        print("It's a tie")
    if horse3>=50 and horse2>=50 and horse3==horse2 and horse1<horse2 and horse1<horse3:
        print("It's a tie")
main()
