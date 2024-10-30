def the_mag():
    #This program calculates the future value of an investment with compounding interest
    
    
    principal = int(input("Enter the initial principal value"))
    interst_rate = int(input("Enter the annual nominal interest rate"))
    periods = int(input("Enter the number of times the interest is compounded yearly"))
    years = int(input("Enter the number of years for the investment"))

    
    total_periods = years * periods

    for mine in range(total_periods):
        principal = principal * (1 + interst_rate / periods)

    # Print the final value after all periods
    print(f"The value of the investment after" ,years, "years is:",principal)

the_mag()
