def the_blessed():
# This program calculates the future value of an investment with annual contributions
    
    year_investment = int(input("Enter the amount to invest in a year "))
    annual_rate = int(input("Enter the annual interest rate measured in %"))
    year_total = int(input("Enter total investment for the year"))

    total_accumulation = 0

    for m in range(year_total):
        total_accumulation = total_accumulation * (1 + annual_rate)
        total_accumulation += year_investment

    print(f"The total accumulation after {year_total} years is: UGX {total_accumulation}")

the_blessed()
