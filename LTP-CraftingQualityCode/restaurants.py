"""
A restaurant recommendation system.

Here are some example dictionaries. These correspond to the information in
restaurants.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Maxican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str: list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
#dict of {str: list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:
    [[82, 'Queen St. Cafe], [71, 'Dumplings R Us']]
"""

# The file containing the restauratnt data.
FILENAME = 'restaurants.txt'

def recommend(restaurant_file, price, cuisines_list):
    """ (file open for reading, str, list of str) -> list of list of str

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list. Return a list of lists of 
    the form [rating%, restaurant name], sorted by rating%.

    >>> restaurant_file = open('restaurants.txt', 'r')
    >>> recommend(restaurant_file, '$', ['Chinese', 'Thai'])
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(restaurant_file)

    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restauratns that are in the right price range and
    # serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done! Return that sorted list.
    return result
    

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, rstaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87, 'Queen St. Cafe': 82, 'Dumplings R Us': 71, 'Maxican Grill': 85, 'Deep Fried Everything': 52}
    >>> names = ['Dumplings R Us', 'Queen St. Cafe']
    >>> build_rating_list(name_to_rating, names)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]

    """
    
    restaurants_with_rating = []

    for name in names_final:
        rating = name_to_rating[name]
        restaurants_with_rating.append([rating, name])

    return sorted(restaurants_with_rating, reverse = True)


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    Return a list of restaurant names that serve of of the cuisines.

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'], 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'], 'Malaysian': ['Queen St. Cafe'], 'Thai': ['Queen St. Cafe'], 'Chinese': ['Dumplings R Us'], 'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Dumplings R Us', 'Queen St. Cafe']
    """
    
    matched_restaurants = []

    for cuisine in cuisines_list:
        for name in names_matching_price:
            if name in cuisine_to_names[cuisine]:
                matched_restaurants.append(name)

    return matched_restaurants


def read_restaurants(restaurant_file):
    """ (file open for reading) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}

    >>> restaurant_file = open('restaurants.txt', 'r')
    >>> read_restaurants(restaurant_file)
    ({'Queen St. Cafe': 82, 'Deep Fried Everything': 52, 'Mexican Grill': 85, 'Georgie Porgie': 87, 'Dumplings R Us': 71}, {'$$': ['Mexican Grill'], '$$$$': [], '$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'], '$$$': ['Georgie Porgie']}, {'Malasian': ['Queen St. Cafe'], 'Mexican': ['Mexican Grill'], 'Chinese': ['Dumplings R Us'], 'Canadian': ['Georgie Porgie'], 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'], 'Thai': ['Queen St. Cafe']})
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    lines = restaurant_file.readlines()
#    print lines

    for i in range(0, len(lines), 5):
        restaurant_name = lines[i].rstrip('\n')
        rating = int(lines[i + 1].rstrip('\n').rstrip('%'))
        price = lines[i + 2].rstrip('\n')
        cuisine_names = lines[i + 3].rstrip('\n').split(', ')

        name_to_rating[restaurant_name] = int(rating)
#        print name_to_rating
        price_to_names[price].append(restaurant_name)
#        print price_to_names

        for cuisine_name in cuisine_names:
            if cuisine_name in cuisine_to_names:
                cuisine_to_names[cuisine_name].append(restaurant_name)
            else:
                cuisine_to_names[cuisine_name] = [restaurant_name]

    return (name_to_rating, price_to_names, cuisine_to_names)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

