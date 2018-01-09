"""Restaurant rating lister."""

import sys
import random


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
        # new_restaurant_score = raw_input(
        #                  "How would you rate the restaurant on a scale of 1 to 5? ")
        # if new_restaurant_score.isdigit() and 1 <= int(new_restaurant_score) <= 5:
        #     break
        # else:
        #     print "Please enter a number between 1 and 5"
        try:
            new_restaurant_score = int(raw_input(
                        "How would you rate the restaurant on a scale of 1 to 5? "))
        except ValueError:
            print "Please enter an integer."
        else:
            if 1 <= new_restaurant_score <= 5:
                break
            else:
                print "Please enter a number between 1 and 5"

    restaurant_ratings_dict[new_restaurant_name] = new_restaurant_score

    print_restaurant_ratings(restaurant_ratings_dict)

    return restaurant_ratings_dict


def update_restaurant_rating(restaurant_ratings_dict):
    """Updates a restaurant's rating"""

    # restaurant_to_update = random.choice(restaurant_ratings_dict.keys())

    while True:
        restaurant_to_update = raw_input("What restaurant would you like to update? ")

        if restaurant_to_update in restaurant_ratings_dict:
            break
        else:
            print "Sorry, that restaurant isn't in our list. Please try again."

    print "{} is rated at {}.".format(restaurant_to_update,
                                restaurant_ratings_dict[restaurant_to_update])

    while True:
        try:
            new_rating = int(raw_input("What would you like to change this rating to? "))
        except ValueError:
            print "Please enter an integer."
        else:
            if 1 <= new_rating <= 5:
                break
            else:
                print "Please enter a number between 1 and 5"

    restaurant_ratings_dict[restaurant_to_update] = new_rating

    print "Great! Now, {} is rated at {}.".format(restaurant_to_update,
                                restaurant_ratings_dict[restaurant_to_update])

def create_yelp_knockoff(restaurant_ratings_dict):
    """Allows user to rate restaurants and view ratings"""

    while True:

        user_choice = raw_input("""What would you like to do?
            A) View all restaurant ratings
            B) Add a new restaurant
            C) Update a restaurant rating
            Q) Quit
            > """).lower()

        if user_choice == 'q':
            print "Okay, bye!"
            break

        elif user_choice == 'a':
            print_restaurant_ratings(restaurant_ratings_dict)

        elif user_choice == 'b':
            add_new_restaurant(restaurant_ratings_dict)
        elif user_choice == 'c':
            update_restaurant_rating(restaurant_ratings_dict)
        else:
            print "Please enter A, B, C or Q."


restaurant_ratings_dict = create_restaurant_ratings_dict(sys.argv[1])
create_yelp_knockoff(restaurant_ratings_dict)
