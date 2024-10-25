salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for current in range(1, months+1): # current - текущий месяц
    if current > 1:
        spend *= (increase + 1)
    debt = salary - spend
    money_capital -= debt




print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
