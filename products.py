class Product:
    def __init__(self, name: str, price: float, quantity: int, active: bool = True):
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
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self) -> None:
        print(f"{self.name} - ${self.price} - {self.quantity} in stock")

    def buy(self, quantity: int) -> float:
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
