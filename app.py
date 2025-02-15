class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Using setter to validate price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def apply_discount(self, percent):
        """Apply a discount to the product price"""
        if percent < 0 or percent > 50:
            print("Invalid discount! Maximum allowed is 50%.")
            return
        self.price -= self.price * (percent / 100)
        print(f"Discount applied! New price: €{self.price:.2f}")

    def display_info(self):
        """Display product details"""
        print(f"Product: {self.name}")
        print(f"Price: €{self.price:.2f}")

if __name__ == "__main__":
    product = Product("Laptop", 1000)
    product.display_info()
    product.apply_discount(20)
    product.display_info()






