## Функции

# Задание №2
def format_price(price):
    price=int(price)
    return(f'Цена: {price} руб.')
fix_price = format_price(56.24)
print(fix_price)