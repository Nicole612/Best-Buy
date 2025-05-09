class Product:

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
        return  self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        return self.active


    def activate(self) -> bool:
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        if quantity < 1:
            raise ValueError("You must buy at least one product")
        if self.quantity < quantity:
            raise ValueError("It is not enough product on stock")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price