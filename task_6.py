profit = int(input('Введите прибыль компании: '))
costs = int(input('Введите издержки компании: '))
staff = int(input('Введите количество сотрудников в вашей компании: '))
if profit > costs:
    profitability = (profit - costs)/profit
    print(f'Прибыль вашей компании составляет: {profit - costs}, рентабельность составила: {profitability},прибыль на одного сотрудника: {(profit - costs)/staff}')
elif profit < costs:
    print(f'Компания отработала в убыток на {profit - costs}')
else:
    print(f'Компания отработала в ноль')