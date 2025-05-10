class Product:
    """ Represents a product in the store.

        Attributes:
            name (str): The name of the product.
            price (float): The price per unit of the product.
            quantity (int): The available quantity of the product in stock.
            active (bool): Indicates whether the product is currently active.

        Methods:
            get_quantity()
            set_quantity(quantity)
            is_active()
            activate()
            deactivate()
            show()
            buy(quantity)

        """
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Productname can not be empty")

        if price < 0:
            raise ValueError("Price can not be negative")

        if quantity < 0:
            raise ValueError("Quantity can not be negative"
                             "")
        self.active = True
        self.name = name
        self.price = price
        self.quantity = quantity


    def get_quantity(self) -> int:
        """ Returns the current quantity of the product."""
        return  self.quantity


    def set_quantity(self, quantity):
        """ Updates the quantity and deactivates the product if it reaches zero. """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """ Returns whether the product is active. """
        return self.active


    def activate(self) -> bool:
        """ Sets the product status to active. """
        self.active = True


    def deactivate(self):
        """ Sets the product status to inactive. """
        self.active = False


    def show(self):
        """ : Returns a formatted string representation of the product. """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """ Processes the purchase of a given quantity and returns the total price. """
        if quantity < 1:
            raise ValueError("You must buy at least one product")
        if self.quantity < quantity:
            raise ValueError("It is not enough product on stock")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price
