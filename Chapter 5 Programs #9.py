#9
from random import randrange
def main():
    count1=0
    count2=0
    for x in range (1,101):
        flip=randrange(1,3)
        if flip == 1:
            count1=count1+1
        if flip ==2:
            count2=count2+1
    print("Number of heads:", count1)
    print("Number of tails", count2)
main()