"""
Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to 
organize some of your sales data.
"""

# Your code below:
### Making some pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
print()

### Finding $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print()

### Finding the length of the toppings list
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizzas!")
print()

### Pizza toppings & prices 2D list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
print()

### Sorting list in ascending order
pizza_and_prices.sort()

### Get the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("Cheapest pizza:", cheapest_pizza)
print()

### Get the most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print("Pricest pizza:", priciest_pizza)
print()

### Removing a topping from the list
pizza_and_prices.pop()

### adding a new topping to the list
pizza_and_prices.insert(3,[2.5, "peppers"])
print()

### Finding the three cheapest slices
three_cheapest = pizza_and_prices[:3]
print("Three cheapest pizzas:", three_cheapest)
print()

print(pizza_and_prices)