price = 0
amount_of_tickets = (int(input("Введите количество билетов:\n")))

for tickets in range(amount_of_tickets):
    age = (int(input("Введите возраст посетителя:\n")))
    if age < 18:
        price += 0
    elif 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390

if amount_of_tickets > 3:
    discount = price / 100 * 10
    final_price = price - discount
    print("Скидка составляет:", discount, "руб.")
    print("К оплате:", final_price, "руб.")
else:
    print("Без скидки.К оплате:", price, "руб.")
