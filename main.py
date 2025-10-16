from products import Product
from store import Store


def start(store: Store):
    while True:
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            print("\nAvailable Products:")
            for product in store.get_all_products():
                product.show()
        elif choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal quantity in store: {total}")
        elif choice == "3":
            shopping_list = []
            products = store.get_all_products()
            print("\nEnter the product number and quantity to order. Leave empty to finish.")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.name} (price: ${product.price}, quantity: {product.quantity})")
            while True:
                prod_num = input("Product number (or press enter to finish): ").strip()
                if prod_num == "":
                    break
                if not prod_num.isdigit() or not (1 <= int(prod_num) <= len(products)):
                    print("Invalid product number. Try again.")
                    continue
                product = products[int(prod_num) - 1]
                qty_str = input(f"Quantity of '{product.name}': ").strip()
                if not qty_str.isdigit() or int(qty_str) <= 0:
                    print("Invalid quantity. Try again.")
                    continue
                qty = int(qty_str)
                shopping_list.append((product, qty))
            if shopping_list:
                try:
                    total_cost = store.order(shopping_list)
                    print(f"\nOrder successful! Total cost: ${total_cost}")
                except Exception as e:
                    print(f"Order failed: {e}")
            else:
                print("No items ordered.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
