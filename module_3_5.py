# module_3_5.py Самостоятельная работа по уроку "Рекурсия"
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        first = 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(40203000)
print(result)
result = get_multiplied_digits(560004500001)
print(result)
result = get_multiplied_digits(560004000050000)
print(result)
