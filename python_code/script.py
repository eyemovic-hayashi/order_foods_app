from food_menu import Food

food1 = Food('ハンバーガー', 100)
food2 = Food('チーズバーガー', 150)
food3 = Food('フィッシュバーガー', 200)

foods = [food1, food2, food3]

index = 0

for food in foods:
  print(str(index) + ':' + food.info())
  index += 1

print('--------------------')

order = int(input('メニューの番号を選んでください：'))
order_food = foods[order]

print('選んだfoodは「' + order_food.name + '」です')

food_count = int(input('注文個数を入力してください：'))

result = order_food.get_total_price(food_count)

print('合計金額は、'+ str(result) + '円です。')