#22
from random import randrange
def main():
    hval1,hval2,hval3=eval(input("Enter 3 numbers between 1 and 3 separated by a comma "))
    sum=hval1+hval2+hval3
    compsum=0
    money=50
    r1=randrange(1,4)
    r2=randrange(1,4)
    r3=randrange(1,4)
    compsum=r1+r2+r3
    print("You have $50 to play")
    while (money<0 and money>100):
        print("The computer's number is:",r1)
        print("The computers number is",r2)
        print("The computer's number is", r3)
        print("The sum of your number is",sum )
        print("The computer's sum is", compsum)
    if sum==compsum:
         print("You've won $20! Your total balance is $", money+20)
         hval1,hval2,hval3=eval(input("Enter 3 numbers between 1 and 3 separated by a comma "))
    if sum != compsum:
        print("You've lost. Your total balance is $", money-10)
        hval1,hval2,hval3=eval(input("Enter 3 numbers between 1 and 3 separated by a comma "))
main()


