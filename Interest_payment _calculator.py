def main():
    print("Welcome to interest payment calculator...")
    print("")

    lone_amount = float(input("Enetr Your amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Input amount of years: "))


    monthly_interest_rate = apr/1200
    amount_months = years*12
    monthly_payment = lone_amount*monthly_interest_rate/(1-(1+ monthly_interest_rate)**(-amount_months))
    print("The monthly payment of the loan is: %.2f" % monthly_payment)
while True:    
    main()


