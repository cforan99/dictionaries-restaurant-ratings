# your code goes here

""" Print a list of restaurants and their ratings from a text file_name

First iterate through the file line by line, split the restaurant name from ratings. 
Add the key value pairs to a dictionary. Once inside the dictionary, sort alphabetically 
by restaurant name. Print a list formatted as a sentence."""

text_file = open("scores.txt")

restaurant_scores = {} #created a dictionary

for line in text_file:
    line = line.rstrip()
    restaurant_info = line.split(':')  ##restaurant_info (name&score) = is being saved as a list and the information is being save temp as a list
    name, score = restaurant_info #unpacking the list and assiging variables to item in the list 
    restaurant_scores[name] = int(score) #we are adding the restaurant by line into dictonary

restaurant_scores_list = restaurant_scores.items()  ##here we changed (dictionary)
                                                    ##restaurant_score into a list of tuples, and assigned a new name. 

restaurant_scores_list.sort() #we wanted to keep same list but sort it in place. 

for name, score in restaurant_scores_list: #unpacked the tuple, the first is a name, and score
    print "{} is rated at {}.".format(name, score)