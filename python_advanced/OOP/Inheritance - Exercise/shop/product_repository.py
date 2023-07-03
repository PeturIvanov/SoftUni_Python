from shop.product import Product


class ProductRepository:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        products_date = "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
        return f"{products_date}"