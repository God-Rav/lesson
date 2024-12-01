# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

# Задайте переменные разных типов данных:
immutable_var = (44, 'hello', 1,5)
print(immutable_var)


#  Изменение значений переменных:
# immutable_var = (44, 'hello', 1,5)
# immutable_var[0] = 888
# print(immutable_var)

# если попытаться изменить элемент кортежа, нам выдаст ошибку что (объект "кортеж" не поддерживает назначение элементов)
# т.к кортеж относится к типу данных tuple. А это один из типов данных который относится к неизменяемым объектам.



# Создание изменяемых структур данных:
mutable_list = ('яблоко', 'апельсин', ['Груша'])
mutable_list[2][0] = 'Шаурма'
print('Кортежный список, с изменяемым списком внутри: ', mutable_list)



# result
# (44, 'hello', 1, 5)
# Кортежный список, с изменяемым списком внутри:  ('яблоко', 'апельсин', ['Шаурма'])
