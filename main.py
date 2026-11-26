import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)

def start(shop):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(shop)
        elif choice == "2":
            print(f"Total of {shop.get_total_quantity()} items in store")
        elif choice == "3":
            make_order(shop)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice, please try again.")

def list_products(shop):
    active_products = shop.get_all_products()
    print("------")
    for number, product in enumerate(active_products, start=1):
        print(f"{number}. ", end="")
        product.show()
    print("------")

def make_order(shop):
    list_products(shop)
    active_products = shop.get_all_products()
    shopping_list = []

    print("When you want to finish the order, enter an empty text.")
    while True:
        product_number = input("Which product # do you want? ")
        if product_number == "":
            break
        amount = input("What amount do you want? ")

        try:
            product = active_products[int(product_number) - 1]
            shopping_list.append((product, int(amount)))
            print("Product added to list!")
        except (ValueError, IndexError):
            print("Invalid input, please try again.")

    if shopping_list:
        try:
            total_price = shop.order(shopping_list)
            print(f"********\nOrder made! Total payment: {total_price} dollars")
        except ValueError as error:
            print(f"Error while making order: {error}")

if __name__ == "__main__":
    start(best_buy)
    """Zeigt das Menü und führt die Auswahl aus."""
