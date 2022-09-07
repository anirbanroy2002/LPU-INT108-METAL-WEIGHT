metal = input("Kindly choose a metal (Iron/Aluminium/Zinc/Copper): ").lower()
if metal != "iron" and metal != "aluminium" and metal != "zinc" and metal != "copper":
    print("Sorry, that's not a valid metal from the list. Please try again.")
    exit()
shape = input("Kindly choose between a cube or a cuboid: ").lower()
if shape != "cube" and shape != "cuboid":
    print("Sorry, that's not a valid shape from the list. Please try again.")
    exit()

metal_densities = {"iron": 7.8, "aluminium": 2.7, "zinc": 7.1, "copper": 8.9} # in g/cm^3
if metal != "iron" and metal != "aluminium" and metal != "zinc" and metal != "copper":
    print("Sorry, that's not a valid metal from the list. Please try again.")
    exit()

if shape == "cube":
    side = float(input("Enter the length of a side in cm: "))
    volume = side ** 3
    weight = volume * metal_densities[metal]
else:
    length = float(input("Enter the length in cm: "))
    width = float(input("Enter the width in cm: "))
    height = float(input("Enter the height in cm: "))
    volume = length * width * height
    weight = volume * metal_densities[metal] 

print ("The weight of the", metal, shape, "is", weight, "grams.")

      