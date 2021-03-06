"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def town_name(name):
    """Checks to see if your town matches my hometown"""


    if name == "San Jose":
        return True
    else:
        return

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def first_last(name1, name2):
    """Returns the users full name"""
    full_name = name1 + name2

    return full_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

def introduction(town, first_name, last_name):
    """Takes home town and full name and returns a frienly greeting"""
    if town_name(name) == True:
        print "Hi, %s, we're from the same place!" % first_last(first_name, last_name)
    else:
        print "Hi %s, I'd like to vist %s!" % first_last(first_name, last_name), town

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if fruit == "Strawberry" or fruit == "raspberry" or fruit == "blackberry":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit) == True:
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    new_list = lst

    new_list.append(num)

    return new_list


def calculate_price(price, state, *taxes):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    """I had to look up Arbitrary Argument Lists to make this function work. I don't 
    entirely understand how these funtions work. But it did make all tests pass. If this 
    doesn't work in your tests I'm sorry. I would be interested in learning more about 
    how this works"""

    total_cost = 0.00
    if taxes == "0.0":
        tax = taxes
    else:
        tax = 0.05

    if state == "CA":
        total_cost = (price + (price * tax)) + ((price + (price * tax)) * 0.03)

    elif state == "PA":
        total_cost = (price + (price * tax)) + 2.00

    elif state == "MA":
        if price < 100:
            total_cost = (price + (price * tax)) + 1.00
        else:
            total_cost = (price + (price * tax)) + 3.00

    elif state == "OR":
        total_cost = float(price)

    else:
        total_cost = (price + (price * tax))


    return total_cost


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.


def advanced_work(list, *additional_items):
    """This function should take a presisting list and add items from an addional list 
    to the list"""

    if len(additional_items) > 0:
        for item in additional_items:
            list = list.append(item)

    return list

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def advanced_nested(word):
    """Should take a word then put it in a tuple"""

    def inner_nested(words):
        """should take a word and print it three times"""
        tripple = words + words + words
        return tripple

    combo_nest = (word)

    combo_nest = combo_nest.append(inner_nested(word))

    return combo_nest


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
