money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение
whole_money = money_capital
while whole_money >= spend:
    month += 1
    whole_money = salary + whole_money
    spend *= 1.05
    whole_money = whole_money - spend
  
print(month)
