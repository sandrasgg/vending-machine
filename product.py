


class Product:
    def __init__(self, order: int, name: str, price: float, stock: int):
        self.order = order
        self.name = name
        self.price = price
        self.stock = stock
    
    def decrease_stock(self) -> None:
        if self.stock == 0:
            pass
        else:
            self.stock -= 1
