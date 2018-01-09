"""Restaurant rating lister."""

import sys


def create_restaurant_ratings_dict(filename):
    """Takes a file with restaurant ratings and creates a dictionary"""

    restaurant_ratings_dict = {}

    with open(filename) as restaurants:
        for line in restaurants:
            line = line.rstrip()
            restaurant_entry = line.split(":")
            restaurant_ratings_dict[restaurant_entry[0]] = restaurant_entry[1]

    return restaurant_ratings_dict


def print_restaurant_ratings(restaurant_ratings):
    """Prints a list of restaurants and their ratings

    parameter: dictionary of restaurants and ratings
    """

    restaurant_ratings_list = sorted(restaurant_ratings.items())

    for restaurant, rating in restaurant_ratings_list:
        print "{} is rated at {}.".format(restaurant, rating)


def add_new_restaurant(restaurant_ratings_dict):
    """Adds new restaurant and rating based on user input"""

    new_restaurant_name = raw_input("What restaurant do you want to add? ")

    while True:
        try:
            new_restaurant_score = int(raw_input(
                        "How would you rate the restaurant on a scale of 1 to 5? "))
        except ValueError:
            print "Please enter an integer."
        else:
            if 0 < new_restaurant_score < 6:
                break
            else:
                print "Please enter a number between 1 and 5"

    restaurant_ratings_dict[new_restaurant_name] = new_restaurant_score

    print_restaurant_ratings(restaurant_ratings_dict)

    return restaurant_ratings_dict


restaurant_ratings_dict = create_restaurant_ratings_dict(sys.argv[1])
add_new_restaurant(restaurant_ratings_dict)

