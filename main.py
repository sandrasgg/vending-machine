from product import Product
from machine import Machine
from utils import clear


def init():

    machine = Machine()
    product1 = Product(1, 'Coke', 2.50, 1)
    product2 = Product(2, 'Fanta', 2.50, 2)
    product3 = Product(3, 'Sprite', 2.20, 3)
    product4 = Product(4, 'Aquarius', 2.45, 2)
    product5 = Product(5, 'Lemonade', 2.25, 1)
    product6 = Product(6, 'Water', 2, 1)
    machine.add_product(product1)
    machine.add_product(product2)
    machine.add_product(product3)
    machine.add_product(product4)
    machine.add_product(product5)
    machine.add_product(product6)

    clear()
    print("\nWelcome to the Vending Machine!\n")
    while machine.working == True:
        machine.show_products()
        try:
            choice = input("\nPlease select a product: \n> ").capitalize()
            if machine.is_product_available(choice):
                beverage = machine.select_product(choice)
                machine.insert_coins(beverage)
                machine.buy_product(beverage)
                if machine.is_empty():        
                    machine.refund()              
                else:                         
                    keep_buying = input("\nDo you want to buy something else? (y/n): \n> ").lower()
                    if keep_buying == 'n':
                        machine.refund()
                        
                    if keep_buying == 'y':
                        clear()
                        continue

        except AttributeError:
            print("\n*** Please enter a product name or number ***")


init()
