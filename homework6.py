my_dict = {'Helen': 1995, 'Victor': 2001, 'Ola': 2020}
print(my_dict)
print(my_dict.get('Victor'))
print(my_dict.get('Kiril'))
my_dict.update({'Dima': 2023})
my_dict['Mihei'] = 2002
a = my_dict.pop('Helen')
print(a)
print(my_dict)

my_set = {2, 20, 20, 30, 30, 40, 40, (1, 2, 3), (1, 2, 3), 'Helen', 'Helen', False, False}
print(my_set)
my_set.add(True)
my_set.add(777)
my_set.remove(False)
print(my_set)
