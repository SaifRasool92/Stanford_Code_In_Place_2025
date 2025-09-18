"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then
prints the equivalent weight on that planet.

Note that the user should type in a planet with
the first letter as uppercase, and you do not need
to handle the case where a user types in something
other than one of the planets (that is not Earth).
"""

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Prompt the user for their weight on Earth
<<<<<<< HEAD
    earth_weight = float(input("Enter  your weight on Earth? "))
=======
    planet_weight=  float(input("Enter your weight on Earth ")) #typecasting
    
>>>>>>> ffae62997db85ab7574aec5abd432826eb30f46c

    # Prompt the user for the name of a planet
    planet=input("Enter Your planet name ")
    

    # Determine the gravitational constant for the selected planet
    if planet == "MERCURY":
      gravity_constant=MERCURY_GRAVITY


    elif planet == "VENUS":
      gravity_constant=VENUS_GRAVITY
    elif planet == "MARS":
      gravity_constant=MARS_GRAVITY
    elif planet == "JUPITER":
      gravity_constant=JUPITER_GRAVITY
    elif planet == "SATURN":
      gravity_constant=SATURN_GRAVITY
    elif planet == "URANUS":
      gravity_constant=URANUS_GRAVITY

    else:
      gravity_constant=NEPTUNE_GRAVITY
    # Calculate the equivalent weight on the selected planet
    planetary_weight = planet_weight * gravity_constant # formula
    rounded_planetary_weight = round(planetary_weight, 2) # rounding

    # Print the result
    print(f"The equivalent weight on {planet}:  {rounded_planetary_weight}")  # concatenate

if __name__ == "__main__":
    main()
