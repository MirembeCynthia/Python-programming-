print("Celsius to Fahrenheit Conversion Table")
print("Celsius\tFahrenheit")  

for celsius in range(0, 101, 5):  
    fahrenheit = 9/5 * celsius + 32
    print(f"{celsius}\t{fahrenheit:.1f}")