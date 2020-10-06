# python vending_machine.py

class Product:
    def __init__(self, order, name, price, stock):
        self.order = order
        self.name = name
        self.price = price
        self.stock = stock
    
    def decreaseStock(self):
        if self.stock == 0: #pass if the product's stock is already 0
            pass
        else:
            self.stock -= 1 #else, subtract 1 from the product's stock


class Machine: #methods are in alphabetical order
    def __init__(self):
        self.validCoins = 0.0
        self.insertedCoins = 0
        self.products = []
        self.remainingCash = 0.0
        self.working = True
        
    def addProduct(self, product):
        self.products.append(product) #add the product

    def buyProduct(self, product):
        if self.validCoins >= product.price: #if there is enough money to buy the product
            self.validCoins = self.validCoins - product.price #subtract the price from the user's inserted coins
            self.remainingCash = self.validCoins #calc the change
            product.decreaseStock() #call this method to subtract one from the product.stock
            print('\nYou just bought ' + product.name) #notify the user of which product has been bought
            print('Cash remaining: {:.2f}'.format(self.remainingCash) , '€ ') #and how much cash remains in the machine

    def checkCoins(self, insertedCoin):
        accepted_coins = [0.05, 0.10, 0.20, 0.50, 1, 2] #coins accepted by the machine
        accepted = False
        display_list = [float(item) for item in accepted_coins]
        for coin in accepted_coins:
            if float(self.insertedCoins) in accepted_coins: #if the inserted float is a valid coin
                accepted = True
                self.validCoins += self.insertedCoins #add the inserted coin amount to valid coins
                break
            elif int(self.insertedCoins) in accepted_coins: #if the inserted int is a valid coin
                accepted = True
                self.validCoins += self.insertedCoins #add the inserted coin amount to valid coins
                break
            else:
                print("\nSorry, we only accept these coins: ") #unless the inserted coin is not a valid coin
                print(' '.join(["{0:0.2f}".format(item) for item in display_list]))
                break                    
        return accepted #return whether coins have been accepted by the machine

    def checkIfAvailable(self, chosen):
        state = False
        for product in self.products: #check every product in products[]
            if str(product.order) in chosen or str(product.name) in chosen: #if the user's input exists either in name or in order
                if product.stock == 0: #if that product is out of stock:
                    print("\nWe're sorry, that product is out of stock. \nPlease select another product.")
                    break
                else: #the product exists and is available
                    state = True
                    break
        return state

    def checkIfEmpty(self):
        state = False
        finalStock = sum(product.stock for product in self.products)
        if finalStock == 0: #if the machine is empty
            print("\nWe're out of stock. Please come back later!")
            state = True #notify and return True
        else:
            pass
        return state

    def exit(self, answer):
        if answer == 'y' or answer == 'Y': #if the answer is yes
            print('\nHave a nice day!\n')
            self.working = False #stop the vending machine
        
    def insertCoins(self, beverage):
        enoughCoins = False
        final_price = beverage.price
        while enoughCoins == False:
            print("\nInserted cash: {:.2f}".format(self.validCoins)) #show valid inserted cash to the user
            try:
                self.insertedCoins = float(input('Please insert {:.2f}'.format(final_price - self.validCoins) + '€ : '))
                if self.checkCoins(self.insertedCoins): #check if the user has inserted a valid coin
                    if float(final_price) <= 0: #there are enough coins for the purchase
                        enoughCoins = True
                    if self.validCoins >= float(final_price):
                        enoughCoins = True
            except ValueError:
                print("\n*** ValueError: Please enter a number ***") #if the user's input is not a number
        return enoughCoins #return whether the machine has received enough coins to complete the purchase
            
    def refund(self):
        cash = self.validCoins
        if cash >= 0.05: #if there's cash remainig in the machine
            print('\n{:.2f}'.format(cash) + "€ were refunded.") #show how much
            print('Thank you!')
            self.validCoins = 0 #and eliminate it from the machine
        answer = input("\nWould you like to exit? (y/n) -")
        self.exit(answer) #call the exit method to confirm that the user wants to exit

    def selectProduct(self, chosen):
        beverage = None
        for product in self.products:
            if chosen in product.name: 
                beverage = product
                break
            elif chosen in str(product.order):
                beverage = product
                break
        print("\nYou selected:", beverage.name) #notify which product the user has selected
        return beverage #and if the product exists, return the product

    def showProducts(self): 
        print("\nAvailable products:\n")
        for product in self.products: #show each item available in products[]
            print("{}- {} .............. Price: {:.2f} €".format(product.order, product.name, product.price))


def init():

    machine = Machine()
    product1 = Product(1, 'Coke', 2.50, 2)
    product2 = Product(2, 'Fanta', 2.50, 2)
    product3 = Product(3, 'Sprite', 2.20, 3)
    product4 = Product(4, 'Aquarius', 2.45, 2)
    product5 = Product(5, 'Lemonade', 2.25, 1)
    product6 = Product(6, 'Water', 2, 1)
    machine.addProduct(product1) # add each product
    machine.addProduct(product2)
    machine.addProduct(product3)
    machine.addProduct(product4)
    machine.addProduct(product5)
    machine.addProduct(product6)

    print("\nWelcome to the Vending Machine!\n")
    while machine.working == True:
        machine.showProducts()
        try:
            choice = input("\nPlease select a product: ").capitalize()
            if machine.checkIfAvailable(choice):
                beverage = machine.selectProduct(choice)
                machine.insertCoins(beverage)
                machine.buyProduct(beverage)
                if machine.checkIfEmpty(): #if the machine is empty
                    machine.refund() #call refund method
                else: #if it's not empty, ask if the user wants to continue buying
                    keepBuying = input("\nDo you want to buy something else? (y/n): ")
                    if keepBuying == 'n' or keepBuying == 'N':
                        machine.refund()
                        
                    if keepBuying == 'y' or keepBuying == 'Y':
                        continue

        except AttributeError:
            print("\n*** Please enter a product name or number ***")

# initial call:
init()


