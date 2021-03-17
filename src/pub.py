class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [1]

    def increase_drink_stock(self, drink):
        self.drinks.append(drink)
    
    def increase_till(self, amount):
        self.till += amount
    
    def sell_drink(self, drink, customer):
        if self.drinks != []:
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)
        return None




    

    
