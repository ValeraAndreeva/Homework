start = float(input('Введите стартовое значкение спортсмена: '))
result = float(input('Введите желаемый результат: '))
days = 1
dev = 1
while dev < result:
    ten_pr = start * 0.1
    progress = start + ten_pr
    dev += progress
    days += 1
print(days)




