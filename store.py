from products import Product


class Store:
    def __init__(self, products: list[Product]):
        self.products = products
        
    def add_product(self, product: Product):
        self.products.append(product)
        
    def remove_product(self, product: Product):
        self.products.remove(product)
        
    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)
    
    def get_all_products(self) -> list[Product]:
        return self.products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price