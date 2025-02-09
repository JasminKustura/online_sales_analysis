from product import Product
from product_manager import ProductManager

#Kreiranje menadzera proizvoda

menager = ProductManager()

#Kreiranje proizvoda
menager.add_product(Product("Laptop", 1500, 3))
menager.add_product(Product("Monitor", 300, 5))
menager.add_product(Product("Tastatura", 50, 20))
menager.add_product(Product("Mis", 30, 15))

#Prikaz svih proizvoda i ukupne vrednosti

menager.display_products()
print(f"Ukupna vrednost proizvoda: {menager.total_inventory_value()}")