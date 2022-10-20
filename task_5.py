profit = int(input('Введите прибыль компании: '))
costs = int(input('Введите издержки компании: '))
if profit > costs:
    print(f'Прибыль вашей компании составляет: {profit - costs}')
elif profit < costs:
    print(f'Компания отработала в убыток на {profit - costs}')
else:
    print(f'Компания отработала в ноль')
