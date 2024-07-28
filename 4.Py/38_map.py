# map (function, iterable)

products = [("shirt", 20.00), ("pants", 25.00), ("jackets", 35.00)]
to_euros = lambda products : (products[0], products[1] * 0.82)
to_dollars = lambda products : (products[0], round((products[1] / 0.82), 2))

store_euros = list(map(to_euros, products) )
store_dollars = list(map(to_dollars, products))

for prod in store_euros:
    print(prod)

for prod in store_dollars:
    print(prod)