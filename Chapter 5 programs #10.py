#10
from random import randrange
def main():
    r=randrange(100,1000)
    hundreds= r//100
    tens=(r//10)%10
    ones=r%10
    sum=hundreds+tens+ones
    print(r,'\t',hundreds, '\t', tens, '\t', ones, '\t', "the sum of your hundreds, tens, and ones place is", sum)
main()


