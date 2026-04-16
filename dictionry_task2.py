
products = {
    "Laptop": 75000,
    "Mobile": 45000,
    "Headphones": 3500
}



for key in products.keys():
    print(key,":",products[key])
    

products["Charger"] = 1200
print("Added new product: Charger - Rs. 1200\n")


products["Mobile"] = 42000
print("Updated Mobile price to Rs. 42,000\n")


total = sum(products.values())

print("=== Final Products List ===")
for product, price in products.items():
    print(f"{product:15} : Rs. {price:,}")

print("-" * 40)
print(f"Total Price of all products = Rs. {total:,}")


print(f"Number of products: {len(products)}")