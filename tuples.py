#tuples are special because they are immutable which provides data integrity. they look like lists but inside () instead of []
my_tup = (1,2,3,4,5)
my_list= [1,2,3,4,5]
print(type(my_tup))
print(len(my_tup))

#you can fill with different variable types
tup2= ('cat', 5, 3.55, ['toys', 'mice', 'catnip'])

#do slicing and indexing
print(my_tup[1])
print(my_tup[-2])

#methods associated with tuples. count=> returns how many time it occurs and index returns at what index it first appears
children = (1,2,1,1,5,3,2)
print(children.count(1))
print(children.index(2))