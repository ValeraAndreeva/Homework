var = int(input('введите число: '))
var_2 = 10 * var + var
var_3 = 100 * var + (10 * var + var)
result = var + var_2 + var_3
print(f"{var} + {var_2} + {var_3} = {result}")

# Подходит только для цифр

var = input('введите число: ')
while var < "0":
    print("Введите число больше 0")
print(f"{var} + {var + var}' + {var + var + var} = {int(var) + int(var + var) + int(var + var + var)}")
