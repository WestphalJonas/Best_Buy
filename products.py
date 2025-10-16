class Product:
    """A product in the store with name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int, active: bool = True):
        """Initialize a Product.

        Args:
            name: Product name (must be non-empty string)
            price: Product price (must be non-negative number)
            quantity: Product quantity (must be non-negative integer)
            active: Whether the product is active (default: True)

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")

        self.name: str = name.strip()
        self.price: float = float(price)
        self.quantity: int = quantity
        self.active: bool = active

    def get_quantity(self) -> int:
        """Get the current quantity of the product.

        Returns:
            Current quantity of the product
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the quantity of the product.

        Args:
            quantity: New quantity (must be non-negative)

        Raises:
            ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        self.quantity = quantity

    def is_active(self) -> bool:
        """Check if the product is active.

        Returns:
            True if product is active, False otherwise
        """
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def show(self) -> None:
        """Display product information."""
        print(f"{self.name} - ${self.price} - {self.quantity} in stock")

    def buy(self, quantity: int) -> float:
        """Buy a specified quantity of the product.

        Args:
            quantity: Quantity to buy (must be positive)

        Returns:
            Total cost of the purchase

        Raises:
            ValueError: If product is not active, quantity is not positive, or insufficient stock
        """
        if not self.active:
            raise ValueError(
                f"Product '{self.name}' is not active and cannot be bought."
            )
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive")
        if quantity > self.quantity:
            raise ValueError(
                f"Not enough '{self.name}' in stock. Requested: {quantity}, Available: {self.quantity}"
            )
        self.quantity -= quantity
        return quantity * self.price
