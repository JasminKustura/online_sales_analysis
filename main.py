from product import Product
from product_manager import ProductManager
from cart import Cart

#Kreiranje menadzera proizvoda

manager = ProductManager()
#Kreiranje proizvoda
manager.add_product(Product("Laptop", 1500, 3))
manager.add_product(Product("Monitor", 300, 5))
manager.add_product(Product("Tastatura", 50, 20))
manager.add_product(Product("Mis", 30, 15))

#Prikaz svih proizvoda i ukupne vrednosti

manager.display_products()
print(f"Ukupna vrednost proizvoda: {manager.total_inventory_value()}")

#Dodavanje korpe u main.py

cart = Cart()

#Dodavanje proizvoda u korpu

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])
cart.add_to_cart(manager.products[3])

#Prikaz korpe i ukupne vrednosti


cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.calculate_total()}")


