inventory = {}
def add_product(product_id, product_name, stock_quantity, unit_price):
    if product_id in inventory:
        print(f"Product ID {product_id} already exists. Updating stock quantity.")
        update_stock(product_id, stock_quantity)
        print(inventory)
    else:
        inventory[product_id] = (product_name, stock_quantity, unit_price)
        print(f"Product {product_name} added with ID {product_id}.")
        print(inventory)
def add_stock(product_id, quantity_to_add):
    if product_id in inventory:
        product_name, stock_quantity, unit_price = inventory[product_id]
        new_stock = stock_quantity + quantity_to_add
        inventory[product_id] = (product_name, new_stock, unit_price)
        print(f"Added {quantity_to_add} to {product_name}. New stock is {new_stock}.")
        print(inventory)
    else:
        print(f"Product ID {product_id} not found in inventory.")
def remove_stock(product_id, quantity_to_remove):
    if product_id in inventory:
        product_name, stock_quantity, unit_price = inventory[product_id]
        if quantity_to_remove > stock_quantity:
            print(f"Cannot remove {quantity_to_remove}. Only {stock_quantity} in stock.")
        else:
            new_stock = stock_quantity - quantity_to_remove
            inventory[product_id] = (product_name, new_stock, unit_price)
            print(f"Removed {quantity_to_remove} from {product_name}. New stock is {new_stock}.")
    else:
        print(f"Product ID {product_id} not found in inventory.")

def generate_inventory_report():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory Report:")
        for product_id, (product_name, stock_quantity, unit_price) in inventory.items():
            print(f"ID: {product_id}, Name: {product_name}, Stock: {stock_quantity}, Price: {unit_price}")
while True:
        print ("\nInventory Management System")
        print("1. Add Product")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Generate Inventory Report")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            product_name = input("Enter Product Name: ")
            stock_quantity = int(input("Enter Stock Quantity: "))
            unit_price = float(input("Enter Unit Price: "))
            add_product(product_id, product_name, stock_quantity, unit_price)

        elif choice == '2':
            product_id = int(input("Enter Product ID to add stock: "))
            quantity_to_add = int(input("Enter quantity to add: "))
            add_stock(product_id, quantity_to_add)

        elif choice == '3':
            product_id = int(input("Enter Product ID to remove stock: "))
            quantity_to_remove = int(input("Enter quantity to remove: "))
            remove_stock(product_id, quantity_to_remove)

        elif choice == '4':
            generate_inventory_report()

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid number (1-5).")
