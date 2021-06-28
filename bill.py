class Item:
    def __init__(self, ID, name, amount, price):
        self.ID = ID
        self.name = name
        self.amount = amount
        self.price = price

class Bill:
    def __init__(self):
        self.items = []

    def addItem(self,item):
        self.items.append(item)

    def checkout(self):
        payable = 0
        for item in self.items:
            payable += (item.amount * item.price)
        return payable
