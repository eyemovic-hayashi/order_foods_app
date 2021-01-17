from food import Food
from drink import Drink

food1 = Food('ハンバーガー', 100, 250)
food2 = Food('チーズバーガー', 150, 300)
food3 = Food('フィッシュバーガー', 200, 320)

foods = [food1, food2, food3]

drink1 = Drink('コーラ', 120, 350)
drink2 = Drink('コーヒー', 150, 350)
drink3 = Drink('ミルク', 80, 200)

drinks = [drink1, drink2, drink3]

print('メニューを表示します')
# print('３点以上ご注文いただくと、総額より一割引となります')
print('--------------------')
print('フードメニュー')
index = 0
for food in foods:
  print(str(index) + ':' + food.info())
  index += 1

index = 0
print('ドリンクメニュー')
for drink in drinks:
  print(str(index) + ':' + drink.info())
  index += 1
print('--------------------')

order = int(input('フードの番号を選んでください：'))
order_food = foods[order]
print('選んだフードは「' + order_food.name + '」です')

order = int(input('ドリンクの番号を選んでください：'))
order_drink = drinks[order]
print('選んだドリンクは「' + order_drink.name + '」です')

food_count = int(input('フードの注文個数を入力してください:'))
drink_count = int(input('ドリンクの注文個数を入力してください:'))

result = order_food.get_total_price(food_count) + order_drink.get_total_price(drink_count)

print('合計金額は、'+ str(result) + '円です。')