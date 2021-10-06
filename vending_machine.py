import os



def clear() -> None:
    os.system('clear')

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


class Machine:
    def __init__(self):
        self.valid_coins = 0.0
        self.inserted_coins = 0
        self.products = []
        self.remaining_cash = 0.0
        self.working = True
        
    def add_product(self, product) -> None:
        self.products.append(product)

    def buy_product(self, product):
        if self.valid_coins >= product.price:                                    
            self.valid_coins = self.valid_coins - product.price                     
            self.remaining_cash = self.valid_coins                                  
            product.decrease_stock()                                               
            print('\nYou just bought ' + product.name)                            
            print('Cash remaining: {:.2f}'.format(self.remaining_cash) , '€ ')
        else:
            clear()     

    def check_coins(self, inserted_coin):
        accepted_coins = [0.05, 0.10, 0.20, 0.50, 1, 2]
        accepted = False
        display_list = [float(item) for item in accepted_coins]
        clear()
        for coin in accepted_coins:
            if float(self.inserted_coins) in accepted_coins:          
                accepted = True
                self.valid_coins += self.inserted_coins                
                break
            elif int(self.inserted_coins) in accepted_coins:          
                accepted = True
                self.valid_coins += self.inserted_coins                
                break
            else:
                clear()                                                    
                print("\nSorry, we only accept these coins: ")       
                print(' '.join(["{0:0.2f}".format(item) for item in display_list]))
                break                    
        return accepted

    def is_product_available(self, chosen):
        state = False
        for product in self.products:                                          
            if str(product.order) in chosen or str(product.name) in chosen:    
                if product.stock == 0:
                    clear()                                         
                    print(f"\nWe're sorry, {product.name} is out of stock. \nPlease select another product.")
                    break
                else:                                                          
                    state = True
                    break
        return state

    def is_empty(self):
        state = False
        total_stock = sum(product.stock for product in self.products)
        if total_stock == 0:
            print("\nWe're out of stock. Please come back later!")
            state = True
        else:
            pass
        return state

    def exit(self, answer):
        if answer == 'y' or answer == 'Y':
            clear()
            print('\nHave a nice day!\n')
            self.working = False
        else:
            clear()
        
    def insert_coins(self, beverage):
        enough_coins = False
        final_price = beverage.price

        while enough_coins == False:
            print("\nInserted cash: {:.2f}".format(self.valid_coins))                  
            try:
                self.inserted_coins = float(input('Please insert {:.2f}'.format(final_price - self.valid_coins) + '€ : \n\n> '))
                if self.check_coins(self.inserted_coins):                               
                    if float(final_price) <= 0:                                      
                        enough_coins = True
                    if self.valid_coins >= float(final_price):
                        enough_coins = True
            except ValueError:                                                        
                print("\n*** ValueError: Please enter a number ***") 

        return enough_coins
            
    def refund(self):
        cash = self.valid_coins
        clear()

        if cash >= 0.05:                                            
            print('\n{:.2f}'.format(cash) + "€ were refunded.")     
            print('Thank you!')
            self.valid_coins = 0

        answer = input("\nWould you like to exit? (y/n) -\n> ").lower()
        self.exit(answer)                                           

    def select_product(self, chosen):
        beverage = None
        for product in self.products:
            if chosen in product.name: 
                beverage = product
                break
            elif chosen in str(product.order):
                beverage = product
                break
        clear()
        print("\nYou selected:", beverage.name)
        return beverage

    def show_products(self): 
        print("\nAvailable products:\n")
        for product in self.products:
            print("{}- {} .............. Price: {:.2f} €".format(product.order, product.name, product.price))


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


