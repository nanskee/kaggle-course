# Question 5

# Now say you can no longer buy fractions of a gallon. (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

# With this new scenario, you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

# One function that you'll need to use to do this is math.ceil(). We demonstrate usage of this function in the code cell below. It takes as a number as input and rounds the number up to the nearest integer.
import math

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = math.ceil(total_sqft / sqft_per_gallon)
    cost = gallons_needed * cost_per_gallon
    return cost

print(get_actual_cost(300, 500, 227, 20))

# with these variables, the actual cost needed is 80$, because we can't buy a partial gallon as similar to the project needs