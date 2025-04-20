def generate_invoice(customer_name,items):
    print(f"Invoice for {customer_name}")
    print("--------------------------------")
    total=0
    for item in items:
        subtotal1 = item['price']*item['qty']
        print(f"{item['name']} * {item['qty']}=Rs {subtotal1}")
        total+=subtotal1
        print(f"Total:Rs {total}")

invoice_items = [

    {"name": "Laptop", "price": 50000, "qty": 1},
    {"name": "Mouse", "price": 1000, "qty": 2},

]

generate_invoice("Dipak Bista",invoice_items)