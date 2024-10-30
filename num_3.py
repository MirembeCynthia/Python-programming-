def the_loop():
    for o in range(5): 
        celsius = float(input("What is the Celsius temperature? "))
        f = 9/5 * celsius + 32
        print(f"Temperature is: {f} degrees fahrenheit.")
    
the_loop()
