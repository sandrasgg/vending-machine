from utils import clear


class Machine:
    def __init__(self):
        self.valid_coins = 0
        self.inserted_coins = 0
        self.products = []
        self.remaining_cash = 0
        self.working = True
        
    def add_product(self, product) -> None:
        self.products.append(product)

    def buy_product(self, product) -> None:
        if self.valid_coins >= product.price:                                    
            self.valid_coins = self.valid_coins - product.price                     
            self.remaining_cash = self.valid_coins                                  
            product.decrease_stock()                                               
            print('\nYou just bought ' + product.name)                            
            print('Cash remaining: {:.2f}'.format(self.remaining_cash) , '€ ')
        else:
            clear()     

    def check_coins(self) -> bool:
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

    def is_product_available(self, chosen: str) -> bool:
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

    def is_empty(self) -> bool:
        state = False
        total_stock = sum(product.stock for product in self.products)
        if total_stock == 0:
            print("\nWe're out of stock. Please come back later!")
            state = True
        else:
            pass
        return state

    def exit(self, answer: str) -> None:
        if answer == 'y' or answer == 'Y':
            clear()
            print('\nHave a nice day!\n')
            self.working = False
        else:
            clear()
        
    def insert_coins(self, beverage) -> bool:
        enough_coins = False
        final_price = beverage.price

        while enough_coins == False:
            print("\nInserted cash: {:.2f}".format(self.valid_coins))                  
            try:
                self.inserted_coins = float(input('Please insert {:.2f}'.format(final_price - self.valid_coins) + '€ : \n\n> '))
                if self.check_coins():                               
                    if float(final_price) <= 0:                                      
                        enough_coins = True
                    if self.valid_coins >= float(final_price):
                        enough_coins = True
            except ValueError:
                clear()                                                        
                print("\n*** ValueError: Please enter a number ***") 

        return enough_coins
            
    def refund(self) -> None:
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

        try:
            print("\nYou selected:", beverage.name)
        except Exception as e:
            pass

        return beverage

    def show_products(self) -> None: 
        print("\nAvailable products:\n")
        for product in self.products:
            print("{}- {} .............. Price: {:.2f} €".format(product.order, product.name, product.price))



