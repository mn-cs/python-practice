# 5. Recursive List Sum
# Design a function that accepts a list of numbers as an argument.
# The function should recursively calculate the sum of all the
# numbers in the list and return that value.

# Create a list with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 . (5 point)

# Create a recursive  function that takes the created  list as an
# argument and returns the sum.  (10 points)

# Display the sum.




def list_sum(lst):
  if not lst:
      return 0
  else:
      return lst[0] + list_sum(lst[1:])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = list_sum(numbers)

print(total)