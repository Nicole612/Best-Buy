from collections import defaultdict
import products

class Store:

    def __init__(self, products):
        if not products:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)
        return total_price



