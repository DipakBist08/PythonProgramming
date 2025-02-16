Fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

search_fruit = "apple"

found = any(search_fruit.lower() == fruit.lower() for fruit in Fruits)

if found:
    print("Yes, fruit available")
else:
    print("Out of stock")
