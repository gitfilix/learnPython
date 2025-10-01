coffee_prices = [('cappuccino', 1.6), ('espresso', 2.2), ('mocca', 1.6), ('starbucks', 2.4)]

for coffee, price in coffee_prices:
    print('kafi',coffee)



def most_expensive_coffee(list_of_prices):

    highest_price = 0
    my_most_expensive_coffee = ''

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price = price
            my_most_expensive_coffee = coffee
        else:
            pass

    return (my_most_expensive_coffee, highest_price)

coffee, price = most_expensive_coffee(coffee_prices)

#result = most_expensive_coffee(coffee_prices)

print('price', price)
print('coffe', coffee)