# shopping_cart.py

#from pprint import pprint
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


now = datetime.datetime.now()
#print("VALID IDS:", valid_ids)

print("---------------------")
print ("TARGET")
print ("www.Target.com")
print ("255 Greenwich St, New York, NY 10007")
print("---------------------")
print ("CHECKOUT AT: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
#found help on how to print datetimes on: https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
print("---------------------")

#print("VALID IDS:", valid_ids)

valid_ids = [str(p["id"]) for p in products] # doing comparisons with string versions of these ids
total_price = 0 
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or 'DONE': " ) # the data input will always be a str

    if selected_id == "DONE":
        break # stops the loop
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("Detected invalid input! Please try again...")
     
print ("SELECTED PRODUCTS:" )

for selected_id in selected_ids:
    selected_ids = [p for p in products if str(p["id"]) == str(selected_id)] #converting both to strings
    selected_id = selected_ids [0]
    total_price = total_price + selected_id["price"]
    total_price_usd = to_usd(total_price)
    tax = total_price * .0875
    tax_usd = to_usd(tax)
    final_price = tax + total_price
    final_price_usd = to_usd(final_price)
    price_usd = to_usd(selected_id['price'])
    print(f"+{selected_id['name']}...{price_usd}")

print("-----------------------------------")
print ("SUBTOTAL:"+ str(total_price_usd))
print ("TAX:" + str(tax_usd))
print ("GRAND TOTAL: " + str (final_price_usd))
print("-----------------------------------")
print ("THANK YOU!! SEE YOU AGAIN SOON")
print("-----------------------------------")
