class Product:
    def __init__(self, product_id, name, description, price):
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("Product ID must be a positive integer.")
        if not name or len(name) == 0:
            raise ValueError("Product name cannot be empty.")
        if not isinstance(description, str) or len(description) == 0:
            raise ValueError("Product description cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Product price must be a non-negative number.")

        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, description, price):
        try:
            product = Product(product_id, name, description, price)
            self.products[product_id] = product
            print("Product added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_product(self, product_id):
        product = self.products.get(product_id)
        if product:
            print(product)
        else:
            print("Product not found.")

    def modify_product(self, product_id, name=None, description=None, price=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if description:
                product.description = description
            if price is not None:
                product.price = price
            print("Product updated successfully!")
        else:
            print("Product not found.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product removed successfully!")
        else:
            print("Product not found.")


def main():
    manager = ProductManager()

    manager.add_product(1, "Laptop", "A high-performance laptop", 1500.00)
    manager.add_product(2, "Phone", "A smartphone with a great camera", 800.00)
    manager.add_product(3, "Mouse", "Wireless mouse", 25.99)

    manager.view_product(1)
    manager.modify_product(2, price=750.00)
    manager.remove_product(3)
    manager.view_product(3)

if __name__ == "__main__":
    main()
