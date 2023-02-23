#17
def main():
    principal=eval(input("Enter the principal amount of the loan "))
    interest=eval(input("Enter the interest rate "))  
    term=eval(input("Enter the term of the loan in months "))
    num1=principal*(interest/12)
    num2=(1-(1+interest/12)**-term)
    print("Principal:", principal)
    print("Interest:", interest)
    print("Term:", term)
    print("{0:<5s}{1:<10.2f}".format("The monthly payment is $", num1/num2))
main()
