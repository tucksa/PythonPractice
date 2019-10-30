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