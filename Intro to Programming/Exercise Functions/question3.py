# Question 3

# You're a home decorator, and you'd like to use Python to streamline some of your work. Specifically, you're creating a tool that you intend to use to calculate the cost of painting a room.

# As a first step, define a function get_cost() that takes as input:

# sqft_walls = total square feet of walls to be painted
# sqft_ceiling = square feet of ceiling to be painted
# sqft_per_gallon = number of square feet that you can cover with one gallon of paint
# cost_per_gallon = cost (in dollars) of one gallon of paint
# It should return the cost (in dollars) of putting one coat of paint on all walls and the ceiling. Assume you can buy the exact amount of paint that you need, so you can buy partial gallons (e.g., if you need 7.523 gallons, you can buy that exact amount, instead of needing to buy 8 gallons and waste some paint). Do not round your answer.

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost

print(get_cost(200, 444, 200, 15))

# So, if the square feet of walls is 200
# square feet of ceiling is 444
# square feet of one gallon of paint can cover is 200 ft
# and the cost per gallons of paint is $15
# it costs 48.300000000000004$ to paint the room

