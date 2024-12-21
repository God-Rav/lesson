# Домашнее задание по уроку "Распаковка позиционных параметров".

# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 'яблоко')
print_params(3, 'груша', False)
print_params(b=25)
print_params(c=[1,2,3])

# 2. Распаковка параметров
values_list = [100, 'содержимое списка', False]
values_dict = {'a': 200, 'b': 'содержимое ключа', 'c': 9.99}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = [5, 'пять']
print_params(*values_list_2, 42)