my_dict = {'Liza': 2015, 'Vova': 2009}
print(my_dict)
print(my_dict['Liza'])
my_dict['Sasha'] = 1988
print(my_dict)
my_dict['Irina'] = 1965
my_dict['Boris'] = 1963
Liza = my_dict.pop('Liza')
print(Liza)
print(my_dict)

my_set = {'a', 'b', 'a', 9, 8, 9, True, False, (1, 2 )}
print(my_set)
my_set.update(['c', 7])
print(my_set.discard('a'))
print(my_set)