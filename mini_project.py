menu = {
    "Pizza": 100,
    "Pasta": 150,
    "Burgar": 200,
    "Salad": 80,
    "Coffee": 130 
}

print("Well come to our Digital Restaurant")
print("Pizza: 100\nPasta: 150\nBurgar: 200\nSalad: 80\nCoffee: 130")


total_order = 0


item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    total_order += menu[item1]
    print(f"Your item {item1} has been added your order")

else:
    print(f"this {item1} item is not available yet")     

another_order = input("Do you want an anoyher item (Yes/No ): ")
if another_order == "Yes":
    item2 = input("Enter the name of item which you want: ")  
    if item2 in menu:
        total_order += menu[item2]
        print(f"Your item {item2} has been added to order")
    else:
         print(f"Ordered item {item2} is not avaialable")      

print(f"The tolat amount of items to pay is {total_order}")         