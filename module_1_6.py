my_dict = {'Илья': 1991,
           'Ирина': 2001,
           'Михаил': 1994}
my_dict.update({'Илиос': 1990, 'Тамара': 1870})
print(my_dict)
print(my_dict['Илья'])
print(my_dict.get('Василий'))
print(my_dict.pop('Ирина'))
print(my_dict)

my_set = {1, 3, 4, 5, 'String', 3, 4}
my_set.add(6)
my_set.add('Илья')
my_set.discard('String')
print(my_set)
