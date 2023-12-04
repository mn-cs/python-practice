# (a). Largest List Item

# Design a function that accepts a list as an argument and returns
# the largest value in the list. The function should use recursion
# to find the largest item.

# Create a list with numbers: 10, 20, 30, 40, 50, 60, 70, 80,  90.
#   (5 points)

# Create a recursive  function that takes a list as an argument.
# Pass created list to the recursive function.  (10 points)

# Display the largest item.




def largest_value(lst):
  if len(lst) == 1:
      return lst[0]
  else:
      return max(lst[0], largest_value(lst[1:]))
    

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

max_num = largest_value(numbers)

print(max_num)