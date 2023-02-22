#11
from random import randrange
def main():
    nickels=randrange(2,6) #generates 2 to 5 nickels. 6 is used to allow 5 ot be chosen
    print(nickels,"nickels")
    dimes=randrange(1,5) # generates 1 to 4 dimes allowing 4 to be used
    print(dimes, "dimes")
    quarters=randrange(0,4) #generates 0 ot 3 quarters allowing 3 to be used
    print(quarters, "quarters")
    dolnickels=nickels*5
    doldimes=dimes*10
    dolquarters=quarters*25
    dollars=(doldimes+dolnickels+dolquarters)/100
    print("{0:<1s}{1:<10.2f}".format("$",dollars))
    if dollars >= 0.99:
        print("You can buy a cheeseburger from the Burger King 99¢ menu")
    else:
        print("you can't buy from the Burger King 99¢ menu")
main()