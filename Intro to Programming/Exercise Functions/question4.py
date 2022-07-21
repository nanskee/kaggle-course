# Question 4

# Use the get_cost() function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:

# 432 square feet of walls, and
# 144 square feet of ceiling.
# Assume that one gallon of paint covers 400 square feet and costs $15. As in Question 3, assume you can buy partial gallons of paint. Do not round your answer.

total_sqft = 432 + 144
gallons_needed = total_sqft / 400
project_cost = 15 * gallons_needed
print(project_cost)

# given the variables and the values above, the project cost 21.599999999999998$