talents = float(input("Enter talents : "))
pounds = float(input("Enter pounds : "))
lots = float(input("Enter lots : "))
gram = (lots * 13.3) + (pounds * (13.3*32)) + (talents * (13.3*32*20))
kilo = int(gram / 1000)
grams = gram % 1000
print("The weight in modern units:")
print(f"{kilo} kilograms and {grams} grams")