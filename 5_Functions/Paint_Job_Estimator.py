# (b) Paint Job Estimator (15 points)

# A painting company has determined that for every 112 square feet of wall space, 
# one gallon of paint and eight hours of labor will be required. The company 
# charges $35.00 per hour for labor.

# Write a program that asks the user to enter the square feet of wall space 
# to be painted and the price of the paint per gallon. (2 points)

# The program should display the following data: (3 points)
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job

# Must use at least 2 functions. One function to get input values, 
# one to display the results and main to invoke these two. (7 points)

# Display/Print the results, using 2 decimal points for money. (3 points)


def main():
  while True:
    try:
      square_feet_of_wall, price_pear_gallon = get_input()
      
      if not square_feet_of_wall > 0 or not price_pear_gallon > 0:
        print("* Enter a velid positive number")
        continue
      else:
        display_results(square_feet_of_wall, price_pear_gallon)
        break

    except ValueError:
        print("* Enter a valid number")
        continue
      
def get_input():
  square_feet_of_wall = float(input("Enter the square feet of wall: "))
  price_pear_galon = float(input("Enter the price of the paint per gallon: "))
  return square_feet_of_wall, price_pear_galon
  
def display_results(wall, price):
  
  gallon_of_paint_required = 1 / 112 * wall
  hours_of_labor_required = 8 / 112 * wall 
  cost_of_paint = gallon_of_paint_required * price
  labor_carges = hours_of_labor_required * 35.00
  total_cost = cost_of_paint + labor_carges

  print("\nResults:")
  print(f"Gallons of paint required: {gallon_of_paint_required:.2f}")
  print(f"Hours of labor required: {hours_of_labor_required:.2f}")
  print(f"Cost of the paint: ${cost_of_paint:.2f}")
  print(f"Labor charges: ${labor_carges:.2f}")
  print(f"Total cost of the paint job: ${total_cost:.2f}")
  
main()


# Test 1:
#      input: Enter the square feet of wall: 112
#             Enter the price of the paint per gallon: 35
#     output: Results:
#             Gallons of paint required: 1.00
#             Hours of labor required: 8.00
#             Cost of the paint: $35.00
#             Labor charges: $280.00
#             Total cost of the paint job: $315.00

# Test 2:
#      input: Enter the square feet of wall: 550
#             Enter the price of the paint per gallon: 27
#     output: Results:
#             Gallons of paint required: 4.91
#             Hours of labor required: 39.29
#             Cost of the paint: $132.59
#             Labor charges: $1375.00
#             Total cost of the paint job: $1507.59