# collect the neede inputs: principal, apr, years to repay.
# calculate the monthly payment
# show to the user

#from re import M


def main():
 print(" This is a monthly loan payment calculator ")
 print("")


 principal = float(input("Input you loan amount: "))
 apr = float(input("Input the annual interest rate: "))
 years = int(input("Input amount of years: "))


 monthly_interest_rate = apr / 1200
 amount_of_months = years * 12 
 monthly_payments = principal * monthly_interest_rate / (1- (1+ monthly_interest_rate) ** (-amount_of_months))


 print(" The monthly payment for this loan is : $%.2f " % monthly_payments)


main()