# def calculate_cart_total(cart_items):
#     total=0
#     for item in cart_items:
#         total+= item['price'] *item['quantity']
#     return total
#
# cart =[
#     {"name":"Book-1","price":200,"quantity":2},
#     {"name":"pen","price":25,"quantity":2}
# ]
#
# total_price =calculate_cart_total(cart)
# print(f"Your Total Bill is :{total_price}")


def cart_total(cart_items):
    total = 0
    for item in cart_items:
        total += item['Price'] * item['Quantity']
    return total

cart =[
    {"Item Name": "Automatic Habits","Price":800,"Quantity":1},
    {"Item Name":"Pen","Price":25,"Quantity":12},
    {"Item Name":"Calculator","Price":1050,"Quantity":1}
]

total_price =cart_total(cart)

print(f"Your Final Bill is :{total_price}")
