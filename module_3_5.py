def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0]) #берем первый символ числа number

    if len(str_number) > 1: #если длинна числа больше 1 знака, выполняем функцию
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
