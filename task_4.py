num = int(input("Введите целое положительное число: "))
max_num = 0
rec = num
while rec > 0:
    division = rec % 10
    if division > max_num:
        max_num = division
    rec //= 10
print(f'{max_num} - самая большая цифра в введенном числе')
