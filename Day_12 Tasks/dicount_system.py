# Original list of shop prices
prices = [100, 200, 300, 400]

# Apply 10% discount only when price > 200; otherwise keep original price
discounted_prices = [price * 0.9 if price > 200 else price for price in prices]

print("Updated prices:", discounted_prices)