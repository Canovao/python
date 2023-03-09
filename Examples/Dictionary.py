from this import d


carEspecs = {
    'num': 123,
    'model': 'xt 95',
    'year': 1978,
    'license': 48230587234199,
    'anotherDictionary': {
        'thing': 'value',
        'num': 456
    },
    'list': ['a', 'b', 7, 3, 9, 8, [1, 2]],
}

dynamicDictionary = dict()
dynamicDictionary['boo'] = 'aaah'
dynamicDictionary['pill'] = 12354

#carEspecs.get('keyIwantToFind', defaultValue if do not find the key)

for keys,values in carEspecs:
    print(keys, values)
