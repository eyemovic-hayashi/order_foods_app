from menu_item import MenuItem

class Drink(MenuItem):
  def __init__(self, name, price, amount):
    super().__init__(name, price)
    self.amount = amount

  def info(self):
    return self.name + ':' + str(self.price) + '円 (' + str(self.amount) + 'ml)'