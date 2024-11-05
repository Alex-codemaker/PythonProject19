def get_multiplied_digits(number):
    str_number = str(int(number))# от
    first = int(str_number[0])# строковое значение
    while str_number.endswith('0'):
        str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits('040203')
print(result)








