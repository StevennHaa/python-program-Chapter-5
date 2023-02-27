#12
from random import randrange
def main():
    low=5000
    high=1
    for x in range(1,51):
        number=randrange(1,5001)
        if number<low:
            low=number
        if number>high:
            high=number
    print(high)
    print(low)
main()
