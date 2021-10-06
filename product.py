


class Product:
    def __init__(self, order, name, price, stock):
        self.order = order
        self.name = name
        self.price = price
        self.stock = stock
    
    def decrease_stock(self) -> None:
        if self.stock == 0:
            pass
        else:
            self.stock -= 1