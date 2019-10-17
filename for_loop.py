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

#iterating through dictionaries
Sarah = {'Profession': 'Developer', 'Language': ['Python', 'Javascript', 'HTML', 'CSS', 'SQL', 'MongoDB'], 'Company': 'Verizon'}
for i in Sarah:
    print(i)
#notice by default it prints the keys. to get the key/value pair then...
for i in Sarah.items():
    print(i)
# you can use tuple unpacking to get back just the values
for key,value in Sarah.items():
    print(value)

#go through the list and remove the vowels
names = ['Sarah', 'Danielle', 'Scott', 'Holly', 'Rebecca', 'Ronald', 'Sharolyn', 'Alexander', 'Aurora']
for i in names:
    new_name = ''
    for l in i:
        if l.lower() != 'a' and l.lower() != 'e' and l.lower() !='i' and l.lower() != 'o' and l.lower() != 'u':
            new_name = new_name + l
    print(new_name)


#Practicing while loops. create a list of 1-100
my_list = []
x= 1
while x < 101:
    my_list.append(x)
    x += 1
else:
    print(my_list)  

# break continue pass

#Pass = do nothing at all. python will not let you have a for loop with a comment in it so you have to include pass if you want to come back
x = [1,2,3]
for i in x:
    #this comment alone will break the code so include pass
    pass
print('Now its a placeholder and I can continue with my code')

# Continue goes to the top of the closest enclosing loop
name = 'Sarah'
for letter in name:
    #the vowels can be removed with continue
    if letter == 'a':
        continue 
    print(letter)

# Break = breaks out of the current closest enclosing loop
for i in my_list:
    if i == 11:
        break
    print(i)