# Write a function that computes the volume of a sphere given its radius
import math
def vol(rad):
    # V = 4/3 pi r^3 
    return (4/3)*(math.pi) * (rad**3)

print(vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low, high):
    if num in range(low,high):
        return f'{num} is inbetween {low} and {high}'
    else:
        return f'Sorry... {num} is not between {low} and {high}'

def ran_bool(num,low, high):
    return num in range(low,high)

print(ran_check(10,2,7))
print(ran_bool(2,2,7))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(st):
    upper_count = 0
    lower_count = 0
    for letter in st:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        else:
            continue
            
    return f'No. of uppercase characters: {upper_count}\nNo. of lowercase characters: {lower_count}'

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    unique = []
    for i in lst:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique

print(unique_list([1,1,1,1,3,4,5,5,6,4,6]))

#Write a Python function to multiply all the numbers in a list.
def mult(num):
    total = 1
    for i in num:
        total *= i 
    return total
    
print(mult([2,2,3]))
