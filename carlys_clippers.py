"""
Carly's Clippers

You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in 
the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

1. hairstyles: the names of the cuts offered at Carly’s Clippers.
2. prices: the price of each hairstyle in the hairstyles list.
3. last_week: the number of purchases for each hairstyle type in the last week.
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

### Price & cuts:
total_price = 0

for price in prices:
  total_price += price
print(f"${total_price}")
print()

# Finding the average hairstyle price
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price}")
print()

# Creating a new list with all prices reduced by $5
new_prices = [price - 5 for price in prices]
print(new_prices)
print()

### Calculating the revenue of Carly's Clippers
total_revenue = 0

for i in range(0, len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print(f"Total Revenue: ${total_revenue}")
print()

# Finding the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")
print()

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts under $30")
print(cuts_under_30)
