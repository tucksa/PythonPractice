#in python indentation is very important. notice the indent for each then portion of the if/then logic

#set variables however you want to get the desired response
sky = 'blue'
clouds = False

# if there are blue skies and no clouds then print beautiful day
if sky == 'blue' and not(clouds):
    print("Wow, it's a beautiful day out!")
# else if sky is blue but there are clouds then print concern for possible bad weather
elif sky == 'blue' and clouds:
    print('Uh oh.... it looks a little cloudy. Hopefully it doesnt rain')
# else you have bad color skies and cloud so print bad weather
else:
    print('Bad weather today...')