price = {"meat":112,"milk":30,"bread":20,"sugar":40}
new_price = {}

for i in price.keys():
    new_price[i] = round(price[i] * 0.87, 2)
print(new_price)
#
# new = {}
# for key, value in price.items():
#     new[value] = key
# print(new)

# x = price.values()
# list(x)
# print(x)
#
# for value in price.values():
#     print(value)