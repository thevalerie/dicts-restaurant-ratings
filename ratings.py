"""Restaurant rating lister."""

import sys


def print_restaurant_ratings(filename):
    """Takes a file with restaurant ratings and prints each one"""

    restaurant_ratings_dict = {}

    with open(filename) as restaurants:
        for line in restaurants:
            line = line.rstrip()
            restaurant_entry = line.split(":")
            restaurant_ratings_dict[restaurant_entry[0]] = restaurant_entry[1]

    restaurant_ratings_list = sorted(restaurant_ratings_dict.items())

    for restaurant, rating in restaurant_ratings_list:
        print "{} is rated at {}.".format(restaurant, rating)

print_restaurant_ratings(sys.argv[1])
