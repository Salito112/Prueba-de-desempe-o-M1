# Inventory Management System in Python
# This program allows users to manage an inventory by adding, querying, updating, deleting products, and calculating the total value.

# Initial inventory with 5 products
inventory = [
{'name': 'table', 'price': 34000.0, 'units': 5},
{'name': 'pads', 'price': 23900.0, 'units': 4},
{'name': 'cloths', 'price': 1500.0, 'units': 15},
{'name': 'bag', 'price': 1000.0, 'units': 20},
{'name': 'pen', 'price': 200.0, 'units': 50}
]

# Display menu options
def show_menu():
    print("\n--- Inventory Management ---")
    print("1. Add product")
    print("2. Query product")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Exit")

# Validate float input
def price_input(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("Price must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Validate integer input
def quantity_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Add product to inventory
def add_product(inventory):
    name = input("Enter product name: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            print("Product already exists. Use update option if needed.")
            return
        price = price_input("Enter product price: ")
        units = quantity_input("Enter product quantity: ")
        inventory.append({'name': name, 'price': price, 'units': units})
        print(f"Product '{name}' added successfully.")
        break
    else:
        print("The product already exists. If you want to modify it, use option 4.")
# Query product by name
def query_product(inventory):
    name = input("Enter product name to search: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            print(f"Product: {item['name']} | Price: ${item['price']:.2f} | Quantity: {item['units']}")
            return
    print("Product not found in inventory.")

# Update product price
def update_price(inventory):
    name = input("Enter product name to update price: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            new_price = price_input("Enter new price: ")
            item['price'] = new_price
            print(f"Price of '{name}' updated successfully.")
            return
print("Product not found in inventory.")

# Delete product from inventory
def delete_product(inventory):
    name = input("Enter product name to delete: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                inventory.remove(item)
                print(f"Product '{name}' deleted.")
                return
            elif confirm=='no':
                print("The product was not eliminated")
            else:
                print("Enter a valid option")
    print("Product not found in inventory.")

# Calculate total inventory value
def calculate_total_value(inventory):
    total = 0.0
    for item in inventory:
        total += item['price'] * item['units']
    print(f"Total inventory value: ${total:.2f}")

# Main function to run menu
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            query_product(inventory)
        elif choice == '3':
            update_price(inventory)
        elif choice == '4':
            delete_product(inventory)
        elif choice == '5':
            calculate_total_value(inventory)
        elif choice == '6':
            print("Exiting program.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()