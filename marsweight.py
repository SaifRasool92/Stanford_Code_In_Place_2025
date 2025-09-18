"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""



"""
37.8/100=0.378
constant
input (str)- float    -formula-> mars_weight->  print

"""
MARS_CONSTANT=0.378
def main():
    earth_weight_str=(input("Enter a weight on Earth: "))
    earth_weight=float(earth_weight_str) #typecasting
    

# 3.57687 -> 3.57
    mars_weight= MARS_CONSTANT* earth_weight
    rounded_earth_weight=round(mars_weight,2)
    

    print(f"The equivalent weight on Mars: {rounded_earth_weight}") #concatenat





    
    

if __name__ == "__main__":
    main()
