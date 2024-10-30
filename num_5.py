def The_break():
    #This program calculates the future value of a 10-year investment.
    principal = int(input("Enter the initial principal: "))
    annual_intrest = int(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of year(s): "))
    for k in range(2):
     principal_value = principal * (1 + annual_intrest)
     print("The value in", years ,"years is:",principal_value)
The_break()