class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists.")
        else:
            self.items[item_id] = {"name": name, "quantity": quantity, "price": price}
            print(f"Item {name} added to inventory.")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id not in self.items:
            print(f"Item with ID {item_id} not found.")
        else:
            if quantity is not None:
                self.items[item_id]["quantity"] = quantity
            if price is not None:
                self.items[item_id]["price"] = price
            print(f"Item {self.items[item_id]['name']} updated.")

    def delete_item(self, item_id):
        if item_id not in self.items:
            print(f"Item with ID {item_id} not found.")
        else:
            del self.items[item_id]
            print(f"Item {item_id} deleted.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item_id, details in self.items.items():
                print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

# Example usage
inventory = Inventory()
inventory.add_item("A123", "Laptop", 50, 1200.00)
inventory.add_item("B456", "Mouse", 200, 25.00)
inventory.view_inventory()
inventory.update_item("A123", quantity=45)
inventory.view_inventory()
inventory.delete_item("B456")
inventory.view_inventory()
