from products import Product


class Store:
    """A store that manages a collection of products and handles orders."""

    def __init__(self, products: list[Product]):
        """Initialize the store with a list of products.

        Args:
            products: List of Product objects to initialize the store with

        Raises:
            TypeError: If products is not a list or contains non-Product objects
        """
        # Type checks
        if not isinstance(products, list):
            raise TypeError("Products must be a list")

        # Validate each product in the list
        for i, product in enumerate(products):
            if not isinstance(product, Product):
                raise TypeError(f"Item at index {i} must be a Product instance")

        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store.

        Args:
            product: Product object to add to the store

        Raises:
            TypeError: If product is not a Product instance
        """
        # Type check
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance")

        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store.

        Args:
            product: Product object to remove from the store

        Raises:
            TypeError: If product is not a Product instance
            ValueError: If the product is not found in the store
        """
        # Type check
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance")

        # Value check
        if product not in self.products:
            raise ValueError("Product not found in the store.")
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

        Raises:
            TypeError: If shopping_list is not a list or contains invalid types
            ValueError: If shopping_list is empty
        """
        # Type checks
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list")

        # Value checks
        if not shopping_list:
            raise ValueError("Shopping list cannot be empty")

        # Validate each item in the shopping list
        for i, item in enumerate(shopping_list):
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError(f"Item at index {i} must be a tuple of (Product, int)")
            product, quantity = item
            if not isinstance(product, Product):
                raise TypeError(f"Product at index {i} must be a Product instance")
            if not isinstance(quantity, int):
                raise TypeError(f"Quantity at index {i} must be an integer")

        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
