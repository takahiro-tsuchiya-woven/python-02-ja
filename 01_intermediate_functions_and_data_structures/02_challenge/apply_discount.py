def apply_discount(products, minimum_price, discount_rate):
    ##filtered_product = [(product["name"], product["price"]) for product in products if product["price"] > minimum_price]
    filtered_product = [(lambda x: (x["name"], x["price"] * (100 - discount_rate) / 100))(product) for product in products if product["price"] > minimum_price]

    return filtered_product

input1 = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]

input2 = [
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]

print(apply_discount(input1, 50, 10))
print(apply_discount(input2, 100, 15))