# Map => using map to squre each number in a list

def square(num):
    print(num**2)
my_nums = [1,2,3,4,5]

list(map(square, my_nums))

# Filter funciton => need to filter by a function that returns either true or false and it will filter based on those parameters

def check_even(num):
    print(num%2 == 0)

nums = [1,2,3,4,5,6]

list(filter(check_even, nums))

# Lambda Expressions => an anonymous function you only plan on using one time
#the square function under map could be written as a lambda fucntion like this:
lambda num : num **2

#so in map it would look like this:
list(map(lambda num: num *2, my_nums))
