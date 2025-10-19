import math

def unit_price(diameter, price):
    area = math.pi * (diameter / 2 / 100) ** 2
    return price / area

d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (euro): "))
d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (euro): "))

u1 = unit_price(d1, d2)
u2 = unit_price(p1, p2)

if u1 < u2:
    print("pizza 1 is cheaper per m*2")
else:
    print("pizza 2 is cheaper per m*2")