#iterating over a list to print out 1-10
iterable = [1,2,3,4,5,6,7,8,9,10]
for i in iterable:
    print(i)

#print out only the even numbers
for i in iterable:
    if i%2 == 0:
        print(i)

#get a running total
my_sum = 0
for i in iterable:
    my_sum = my_sum + i
    print(f'My new total is: {my_sum}')