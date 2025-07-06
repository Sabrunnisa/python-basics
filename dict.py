inventory = {
    "P001": ["Apple", 100, 0.50],
    "P002": ["Banana", 150, 0.30],
    "P003": ["Orange", 90, 0.60],
    "P004": ["Milk", 50, 1.20],
    "P005": ["Bread", 200, 0.80],
}

def add_stock(inventory, product_id, quantity):
    if product_id in inventory:
        inventory[product_id][1] += quantity
        print(f"Added {quantity} to '{inventory[product_id][0]}'. New stock: {inventory[product_id][1]}")
    else:
        print(f"Product ID '{product_id}' not found in inventory.")

def remove_stock(inventory, product_id, quantity):
    if product_id in inventory:
        if inventory[product_id][1] >= quantity:
            inventory[product_id][1] -= quantity
            print(f"Removed {quantity} from '{inventory[product_id][0]}'. New stock: {inventory[product_id][1]}")
        else:
            print(f"Cannot remove {quantity} from '{inventory[product_id][0]}'. Not enough stock.")
    else:
        print(f"Product ID '{product_id}' not found in inventory.")

def generate_low_stock_alert(inventory, threshold):
    low_stock_items = {product_id: details for product_id, details in inventory.items() if details[1] < threshold}
    if low_stock_items:
        print("\nLow Stock Alert:")
        for product_id, details in low_stock_items.items():
            print(f"Product ID: {product_id}, Name: {details[0]}, Stock: {details[1]}, Unit Price: ${details[2]:.2f}")
    else:
        print("No low stock items.")

if __name__ == "__main__":
    add_stock(inventory, "P001", 20)
    add_stock(inventory, "P004", 10)  
    
    remove_stock(inventory, "P002", 50)  
    remove_stock(inventory, "P001", 150) 

    generate_low_stock_alert(inventory, 60) 
