# Question 1

# In the next code cell, create a function get_expected_cost() that has two arguments:

# beds - number of bedrooms
# baths - number of bathrooms
# It should return the expected cost of a house with that number of bedrooms and bathrooms. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
# each bedroom adds 30000 to the expected cost
# each bathroom adds 10000 to the expected cost.

# For instance,

# a house with 1 bedroom and 1 bathroom has an expected cost of 120000, and
# a house with 2 bedrooms and 1 bathroom has an expected cost of 150000.

def get_expected_cost(beds, baths):
    value = 80000 + (30000 * beds) + (10000 * baths)
    return value

print(get_expected_cost(1, 1))
# A house with 1 bedroom and 1 bathroom will costs 120,000$
