tokyo = "JPY", 36, 140

currency, lat, long = tokyo
# _, lat, long = tokyo

# print(currency)
# print(lat)
# print(long)

# currency, *location = tokyo
currency, *_ = tokyo
print(currency)
# print(location)