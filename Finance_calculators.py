#Task 12
#Task Name: Finance_calculators.py
#Written By: Hamza Asad
#Date: 2020/02/17

#This program will allow the user to access two financial calculators which is an investment calculator and home loan repayment calculator

import math
#print out the options between investment or bond
print("Investment   - to calculate the amount of interest you'll earn on interest.")
print("Bond     -to calculate the amount you'll have to pay on a home loan.")

#Request the user to choose between investment or bond
invest_or_bond = input("Choose either 'Investment' or 'Bond' from the menu above to proceed: \n").lower()

#If user chooses investment ask him a few questions regarding investments
if invest_or_bond ==  "investment":

#Deposit amount
    deposit = int(input("How much will you be depositing? \n"))

#interest rate
    interest_rate = int(input("Enter the interest rate you prefer (only number of the interest rate should be added not the '%' sign) \n"))

#number of years
    num_of_years = int(input("Enter the number of years you plan on investing: \n"))

#simple or compound interest
    interest = input("Would you prefer 'simple' interest or 'compound' interest \n").lower()
    if interest == "simple":
        simple_interest =  deposit*(1 + interest_rate*num_of_years)/100
        print("simple interest is: ", simple_interest)
    elif interest == "compound":
        compound_interest = deposit* math.pow((1+interest_rate),num_of_years)/100
        print("Compound interest is: ", compound_interest)

#if user chooses bond ask him a few questions regarding bonds
elif invest_or_bond == "bond":
 #request value of the house from the users
    house_value = float(input("What is the current value of the house: \n"))

 #Request the interest rate
    interest_rate = float(input("What is the interest rate: \n"))

 #Request from the user how much time they nned to repay the bond
    num_of_months = float(input("In how many months will you repay the bond: \n"))

 #calculations of bond repayment
    repayment = ((house_value * math.pow((interest_rate/12) +1, num_of_months)) * (interest_rate/12)) / ((math.pow(interest_rate/12 + 1, num_of_months)-1))
    final_bond = repayment/12
    print(f"Your total bond repayment is: R{final_bond:.2f}")







    


