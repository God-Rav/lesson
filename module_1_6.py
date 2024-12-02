# Практическое задание по теме: "Словари и множества"

# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.

# 2. Работа со словарями:
my_dict = {'Вася': 1990, 'Петя':1993, 'Коля':1996}
print('Dict:', my_dict)
print('Existing value:', my_dict['Вася'])
print('Not existing value:', my_dict.get('Таня'))
my_dict.update({'Света': 1991, 'Катя':1994})
a = my_dict.pop('Вася')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print(' ') # просто отступ

# 3. Работа с множествами:
my_set = {1, 0, 0, 1, 2, 2, 2, 3, 'Хлеб', 2.5}
print('Set:', my_set)
my_set.add(5)
b = (7, 8, 1.9)
my_set.add(b)
print('Modified set:', my_set)

# result:
# Dict: {'Вася': 1990, 'Петя': 1993, 'Коля': 1996}
# Existing value: 1990
# Not existing value: None
# Deleted value: 1990
# Modified dictionary: {'Петя': 1993, 'Коля': 1996, 'Света': 1991, 'Катя': 1994}
 
# Set: {0, 1, 2, 3, 2.5, 'Хлеб'}
# Modified set: {0, 1, 2, 3, 2.5, 5, 'Хлеб', (7, 8, 1.9)}
