class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(p.price for p in self.items)
    
    def display_cart(self):
        for product in self.items:
            print(product.display_info())