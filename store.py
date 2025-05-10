import products

class Store:
    """
        Represents a store that manages a collection of products.

        Attributes:
            products: A list of Product instances currently in the store.

        Methods:
            add_product(product)
            remove_product(product)
            get_total_quantity()
            get_all_products()
            order(shopping_list)
        """

    def __init__(self, product_list):
        if not product_list:
            self.products = []
        else:
            self.products = product_list

    def add_product(self, product):
        """ Adds a new product to the store. """
        self.products.append(product)


    def remove_product(self, product):
        """ Removes a product from the store. """
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """ Returns the total quantity of all products in stock. """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """ Returns a list of all active products. """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        """ Processes a list of (product, quantity) tuples and returns the total order price. """
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)
        return total_price



