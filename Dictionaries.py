my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])

#dictionaries can have different types
products= {'vegetables':{'root': ['carrots', 'beets', 'garlic', 'potatoes'], 'leafy': ['spinach', 'arugala', 'romaine letuce']}, 'fruit': {'citrus': ['oragnes', 'lemons', 'limes'], 'tropical': ['pineapple', 'mango']}}
print(products['fruit']['citrus'])

#you can add to the dictionary using assignment
products['meat'] = {'poultrty': ['chicken', 'turkey'], 'seefood': ['salmon', 'crab', 'shrimp'], 'beef': ['ground beef', 'steak']}
print(products)

#practice functions associated with dictionaries
print(f'\n\n{products.keys()}\n')
print(f'\n{products.values()}\n')
print(f'\n{products.items()}\n')
#notice once you call items they are tuples