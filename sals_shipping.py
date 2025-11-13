"""
Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, 
and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

- Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
- Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
- Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

### Ground Shipping
weight = 41.5


print("- Ground Shipping:")

if weight <= 2:
  ground_cost = (1.5 * weight) + 20.00
elif weight <= 6:
  ground_cost = (3.00 * weight) + 20.00
elif weight <= 10:
  ground_cost = (4.00 * weight) + 20.00
else:
  ground_cost = (4.75 * weight) + 20.00
print("Cost: $" + str(round(ground_cost, 2)))
print()

### Ground Shipping Premium
premium_shipping_cost = 125.00

print("- Ground Shipping Premium:")
print("Cost: $" + str(round(premium_shipping_cost, 2)))
print()

### Drone Shipping
print("- Drone Shipping:")

if weight <= 2:
  drone_cost = (weight * 4.50)
elif weight <= 6:
  drone_cost = (weight * 9.00)
elif weight <= 10:
  drone_cost = (weight * 12.00)
else:
  drone_cost = (weight * 14.25)

print("Cost: $" + str(round(drone_cost, 2)))
print()

### Cheapest Shipping Method
cheapest = min(ground_cost, premium_shipping_cost, drone_cost)

print("- Cheapest Shipping Method:")
if cheapest == ground_cost:
    print('The cheapest option is Ground Shipping: $' + str(ground_cost))
elif cheapest == premium_shipping_cost:
    print('The cheapest option is Ground Shipping Premium: $' + str(premium_shipping_cost))
else:
    print('The cheapest option is Drone Shipping: $' + str(round(drone_cost, 2)))
