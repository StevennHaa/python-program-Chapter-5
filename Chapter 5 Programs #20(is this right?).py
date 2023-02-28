#20
from random import randrange
def main():
    start=4
    forward=0
    backwards=0
    count=0
    while start>0 and start<7:
        r=randrange(1,3)
        print(start)
        if r==1:
            count=count+1
            backwards=backwards+1
            start=start-1
            print("You took a", backwards, "step backwards")
        if r==2:
            count=count+1
            forward=forward+1
            start=start+1
            print("You took a", forward, "step forward")
    print("It took you", count, "steps to get off the bridge")
main()
