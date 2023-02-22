#1
from random import randrange
def main():
    r=randrange(1,100)
    count=0
    guess=eval(input("Guess a number between 1 and 100 "))
    while randrange!=guess:
       count=count+1
       guess=eval(input("Guess a number between 1 and 100 "))
       if guess<r:
           print("Too low. Try again")
       if guess>r:
           print("Too high. Try again.")
       if guess==r:
           print("Correct, it took", count,"tries")
main()