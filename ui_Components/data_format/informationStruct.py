class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.modifier = 1.0

    def changePrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return 'ITEM :{0} x {1} @ ${2:.2f}'.format(self.name, self.amount, self.price)

    def setDiscount(self, discount):
        self.modifier = discount

    def getCost(self):
        return self.modifier * (self.amount * self.price)

    def getCostFormatted(self):
        cost = self.getCost()
        return f"${cost:.2f}"

    def set_name(self, name):
        self.name = name
    
    def set_price(self, price):
        self.price = float(price)

    def set_amount(self, amount):
        self.amount = float(amount)


class InformationStruct:
    companyName = 'ONE ANT FARM'

    def __init__(self, items=None, tax=0):
        if items is None:
            items = []
        self.items = items
        self.tax = tax

    def __str__(self):
        string = self.companyName + '\n'
        for i in self.items:
            string = string + str(i) + "\n"
        return string

    def addItem(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def setTax(self, tax):
        self.tax = tax

    def getTotal(self):
        total = 0
        for i in self.items:
            total = i.getCost() + total
        return total * (1 - self.tax)

    def getTotalFormatted(self):
        total = self.getTotal()
        return f"${total:.2f}"

    def getLength(self):
        return len(self.items)

    def removeItem(self, item):
        self.items.remove(item)