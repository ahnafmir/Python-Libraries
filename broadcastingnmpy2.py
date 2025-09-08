import numpy as np

prices = np.array([250,500,750,1000])
discount = 10
final_prices = prices - (prices*(discount/100))

print(final_prices)

error = np.array([1,2,3,4,np.nan])
print(np.isnan(error))

