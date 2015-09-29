# your code goes here

""" Print a list of restaurants and their ratings from a text file_name

First iterate through the file line by line, split the restaurant name from ratings. 
Add the key value pairs to a dictionary. Once inside the dictionary, sort alphabetically 
by restaurant name. Print a list formatted as a sentence."""

text_file = open("scores.txt")

restaurant_scores = {}

for line in text_file:
    line = line.rstrip()
    restaurant_info = line.split(':')  
    name, score = restaurant_info
    restaurant_scores[name] = score

print restaurant_scores