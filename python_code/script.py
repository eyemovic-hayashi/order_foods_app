from food import Food
from drink import Drink

food1 = Food('注文しない', 0, 0)
food2 = Food('ハンバーガー', 100, 250)
food3 = Food('チーズバーガー', 150, 300)
food4 = Food('フィッシュバーガー', 200, 320)

foods = [food1, food2, food3, food4]

drink1 = Drink('注文しない', 0, 0)
drink2 = Drink('コーラ', 120, 350)
drink3 = Drink('コーヒー', 150, 350)
drink4 = Drink('ミルク', 80, 200)

drinks = [drink1, drink2, drink3, drink4]

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

order_food = int(input('フードの番号を選んでください：'))
if order_food == 0:
  print('フードの注文はありませんでした')
else:
  select_food = foods[order_food]
  print('選んだフードは「' + select_food.name + '」です')
  food_count = int(input('フードの注文個数を入力してください:'))
  print(select_food.name + 'を' + str(food_count) + '個注文しました')

order_drink = int(input('続いてドリンクの番号を選んでください：'))
if order_drink == 0:
  print('ドリンクの注文はありませんでした')
else:
  select_drink = drinks[order_drink]
  print('選んだドリンクは「' + select_drink.name + '」です')
  drink_count = int(input('ドリンクの注文個数を入力してください:'))
  print(select_drink.name + 'を' + str(drink_count) + '個注文しました')

if order_food == 0 and order_drink == 0:
  print('またのご利用お待ちしています')
elif order_food >= 1 and order_drink == 0:
  result = select_food.get_total_price(food_count)
  print('合計金額は、'+ str(result) + '円です。')
elif order_drink >= 1 and order_food == 0:
  result = select_drink.get_total_price(drink_count)
  print('合計金額は、'+ str(result) + '円です。')
else:
  result = select_food.get_total_price(food_count) + select_drink.get_total_price(drink_count)
  print('合計金額は、'+ str(result) + '円です。')
