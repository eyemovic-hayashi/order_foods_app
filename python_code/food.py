from menu_item import MenuItem

class Food(MenuItem):
  def __init__(self, name, price, calorie):
    # super()で親クラスのオーバーライドしたメソッドを呼び出している
    super().__init__(name, price)
    self.calorie = calorie

  def calory_info(self):
    print(self.name + 'のカロリーは' + str(self.calorie) + 'Kcalです')

  def info(self):
    return self.name + ':' + str(self.price) + '円 (' + str(self.calorie) + 'Kcal)'