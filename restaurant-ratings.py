from random import randint

""" Print a list of restaurants and their ratings from a text file_name

First iterate through the file line by line, split the restaurant name from ratings. 
Add the key value pairs to a dictionary. Once inside the dictionary, sort alphabetically 
by restaurant name. Print a list formatted as a sentence."""

#Creating the dictionary
text_file = open("scores.txt")

restaurants = {} 

for line in text_file:
    line = line.rstrip()
    restaurant_info = line.split(':')  ##restaurant_info (name&score) = is being saved as a list and the information is being save temp as a list
    name, score = restaurant_info #unpacking the list and assiging variables to item in the list 
    restaurants[name] = [int(score)] #we are adding the restaurant by line into dictonary

#Turning the dictionary into a list
restaurants_list = restaurants.items()  ##here we changed (dictionary)
                                                    ##restaurant_score into a list of tuples, and assigned a new name. 

#Asks for user's name
user_name = raw_input("What is your name?\n")

#Picking a random restaurant in a way that will not repeat
random_list = restaurants_list

if random_list > 0:
    random_restaurant = random_list.pop(randint(0,(len(random_list)-1)))

#Asks user if they have been to the random restaurant

will_repeat = True

while will_repeat:

    if random_list > 0:
        random_restaurant = random_list.pop(randint(0,(len(random_list)-1)))

    can_review = raw_input("Hi {}! Have you dined at {} before? (y/n)\n".format(user_name, random_restaurant[0]))

    if can_review == 'y':
        average = sum(restaurants[random_restaurant[0]])/len(restaurants[random_restaurant[0]])
        user_rating = int(raw_input("{}'s current rating is {}. How would you rate the restaurant? (1-5)\n".format(random_restaurant[0], average)))
        restaurants[random_restaurant[0]].append(user_rating)
        average = sum(restaurants[random_restaurant[0]])/len(restaurants[random_restaurant[0]])
        print "Thanks for your feedback! Now their rating is {}".format(average)
        will_continue = raw_input("Would you like to review another restaurant? (y/n)\n")
        if will_continue == 'n':
            break

    if can_review == 'n':
        pass

restaurants_list.sort() #we wanted to keep same list but sort it in place. 

for name, score in restaurants_list: #unpacked the tuple, the first is a name, and score
    average_score = sum(restaurants[name])/len(restaurants[name])
    print "{} is rated at {}.".format(name, average_score)