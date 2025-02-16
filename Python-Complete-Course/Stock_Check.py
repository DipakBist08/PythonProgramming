#To Check Baskets are available or not
print("Buy Fruits ")

Fruit_Store = ["Apple","Mango","Litchee","Orange","Grips","Banana","PineApple"]
print(Fruit_Store[-2])
UserInput = input("Search Fruit Name here: ")
In_Stock = any(UserInput.lower() == fruit.lower() for fruit in Fruit_Store)
if   Fruit_Store:
    print("Available")
else:
    print("Out of Stock!!")