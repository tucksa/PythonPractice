#unordered collection of unique elements
myset = set()
myset.add(1)
print(myset)

#if you only want to know unique values you can check with something like this
random_nums = [1,1,1,1,1,2,77,6,3,77,3,2,2,0]
print(set(random_nums))

#is set case sensitive? 
print(set('Mr. Salisburry'))
#included space, '.' 'S' and 's'

print(set([1,1,2,3]))
#doesnt matter if its in a list it will still pull the unique values within the list