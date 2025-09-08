prices = [100,200,300]
final_price = []
discount = 10

for price in prices:
    final_prices= price - (price*discount/100)
    final_price.append(final_prices)

print(final_price)    