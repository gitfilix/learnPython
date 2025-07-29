name = input("what is you name? ")
sales = input(f" Okay {name}, how much did you sale last month? ")
# convert sales string to an integer
sales = int(sales)
print(f"hey, {name}, so your total sales is {sales} $")
commission = round(float(sales  * 13 /100), 2)
print(f"Hey {name} your total commission on your sales is: {commission}")


#more sophisticated solution
name = input("please tell me you name")
sales= int(input("Pleas input your total sales: "))

commission = round(sales * 13 / 100, 2)
print(f"Hey {name}, your commission this month are ${commission}")