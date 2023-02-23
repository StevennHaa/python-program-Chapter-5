#13
from random import randrange
def main():
    odd=0
    even=0
    for x in range (1,1001):
        r=randrange(1,10)
        math=r%2
        if math==0:
            even=even+1
        else:
            odd=odd+1
    print("There are", even, "even integers")
    print("There are", odd, "odd integers")
main()
