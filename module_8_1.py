"""
Функция add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление
этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
"""

def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        if type(a) != str:
            result = str(a) + b
        elif type(b) != str:
            result = a + str(b)
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
