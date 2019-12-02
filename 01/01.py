import math
f = open('input.txt', 'r')
in_data = f.readlines()
fuel = 0
# Part 1
for i in in_data:
    k = int(i)
    module_fuel = math.floor(k/3)-2
    fuel = fuel + module_fuel
print(f"""Fuel part 1: {fuel}""")

# Part 2
fuel = 0
for i in in_data:
    k = int(i)
    module_fuel = 0
    while k > 0:
        k = math.floor(k/3)-2
        if k > 0:
            module_fuel = module_fuel+k
    fuel = fuel + module_fuel
print(f"""Fuel part 2: {fuel}""")

