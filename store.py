from products import Product


class Store:
    """A store that manages a collection of products and handles orders."""

    def __init__(self, products: list[Product]):
        """Initialize the store with a list of products.

        Args:
            products: List of Product objects to initialize the store with
        """
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store.

        Args:
            product: Product object to add to the store
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store.

        Args:
            product: Product object to remove from the store
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Get the total quantity of all products in the store.

        Returns:
            Total quantity of all products
        """
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Get all products in the store.

        Returns:
            List of all Product objects in the store
        """
        return self.products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Process an order and calculate total price.

        Args:
            shopping_list: List of tuples containing (Product, quantity) pairs

        Returns:
            Total price of the order
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
