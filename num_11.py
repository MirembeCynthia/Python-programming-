def error_calc():
    name = input("enter your name")
    print(f"Welcome {name} to the Nabbumba Calculator!")
    
    
    for w in range(100):
        expression = input("Enter a math expression (or 'quit' to exit): ")
        
        if expression.lower() == 'quit':
            print(f"Goodbye {name}!")
            break
        
        
        try:
            result = int(expression)
            print("The result is:", result)
        except:
            print("Error: Please enter a valid math expression.")

error_calc()

