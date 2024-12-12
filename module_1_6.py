my_dict = {'igor' : 2000, 'max' : 2003, 'Misha' : 2009}
print(my_dict['igor'])
my_dict['Genya'] =  2005
my_dict.update({'sasha' : 2004,'ilya' : 2001})
print(my_dict.get('Semen'))
a = my_dict.pop('igor')
print(a)
print(my_dict)


